"""This module represents the Gitlab CI [Job](https://docs.gitlab.com/ee/ci/yaml/README.html#job-keywords)

It contains the general `Job` class as well as a special `TriggerJob` class. The latter one is a subclass
of `Job` but has on the one hand reduced capabilities, on the other hand it has the additional functionality
to trigger other pipelines.

Here is a simple example how you define and use a `Job`:

```python
from gcip import Pipeline, Job

pipeline = Pipeline()
job = Job(stage="build", script="build my artefact")
pipeline.add_children(job, name="artifact")
pipeline.write_yaml()

# stages:
#   - build
# build-artifact:
#   stage: build
#   script: build my artifact
```

A `Job` has always a `script` and at least one of `stage` or `name`.
The `stage` will be used for the name of the stage of the job and the
job name itself, whereas `name` is only used for the job`s name. When adding
a job to a `gcip.core.pipeline.Pipeline` or a `gcip.core.sequence.Sequence`
you can and should define a `name` or `stage` too. This is how you
distinguish between two jobs of the same kind added to a pipeline:

```python
def create_build_job(artifact: str, job_name: str = "artifact", job_stage: str = "build") -> Job:
    return Job(name=job_name, stage=job_stage, script=f"build my {artifact}")

pipeline.add_children(create_build_job("foo"), name="bar")
pipeline.add_children(create_build_job("john"), name="deere")

# stages:
#   - build
# build-artifact-bar:
#   stage: build
#   script: build my foo
# build-artifact-deere:
#     stage: build
#     script: build my john
```

Again `name` or `stage` decide whether to add the string to the
stage of a job or not:

```python
def create_build_job(job_name: str = "artifact", job_stage: str = "build", artifact: str) -> Job:
    return Job(name=job_name, stage=job_stage, script=f"build my {artifact}")

pipeline.add_children(create_build_job("foo"), stage="bar")
pipeline.add_children(create_build_job("john"), stage="deere")

# stages:
#   - build_bar
#   - build_deere
# build-bar-artifact:
#   stage: build_bar
#   script: build my foo
# build-deere-artifact:
#     stage: build_deere
#     script: build my john
```

This also decides whether to run the jobs in parralel or sequential. When using
`stage` and adding the string also to the jobs stage the stages for both jobs
differ. When using `name` only the name of the jobs differ but the name of the stage
remains the same.

An `Job` object has a lot of methods for further configuration of typical Gitlab CI
[Job keywords]/https://docs.gitlab.com/ee/ci/yaml/README.html#job-keywords), like
configuring tags, rules, variables and so on. Methods with names staring with..

* **`set_*`** will initally set or overwrite any previous setting, like `set_image()`
* **`add_*`** will append a value to previous ones, like `add_tags()`
* **`append_*`** will do the same as `add_*`, but for values where order matters. So it
   explicitly adds a value to the end of a list of previous values, like `append_rules()`
* **`prepend_*`** is the counterpart to `append_*` and will add a value to the beginning
  of a list of previous values, like `prepend_rules()`
"""

from __future__ import annotations

import copy
from enum import Enum
from typing import (
    TYPE_CHECKING,
    Any,
    Set,
    Dict,
    List,
    Union,
    AnyStr,
    Mapping,
    Optional,
)
from operator import itemgetter

from . import OrderedSetType
from .need import Need
from .rule import Rule
from .cache import Cache
from .image import Image
from .include import Include
from .artifacts import Artifacts

if TYPE_CHECKING:
    from .sequence import Sequence

__author__ = "Thomas Steinbach"
__copyright__ = "Copyright 2020 DB Systel GmbH"
__credits__ = ["Thomas Steinbach", "Daniel von Eßen"]
# SPDX-License-Identifier: Apache-2.0
__license__ = "Apache-2.0"
__maintainer__ = "Thomas Steinbach"
__email__ = "thomas.t.steinbach@deutschebahn.com"


class Job:
    """This class represents the Gitlab CI [Job](https://docs.gitlab.com/ee/ci/yaml/README.html#job-keywords)

    Attributes:
        script (Union[AnyStr, List[str]]): The [script(s)](https://docs.gitlab.com/ee/ci/yaml/README.html#script) to be executed.
        name (Optional[str]): The name of the job. In opposite to `stage` only the name is set and not the stage of the job.
            If `name` is set, than the jobs stage has no value, which defaults to the 'test' stage.
            Either `name` or `stage` must be set. Defaults to `None`.
        stage (Optional[str]): The name and stage of the job. In opposite to `name` also the jobs stage will be setup with this value.
            Either `name` or `stage` must be set. Defaults to `None`.
    """

    def __init__(
        self,
        *,
        script: Union[AnyStr, List[str]],
        name: Optional[str] = None,
        stage: Optional[str] = None,
    ):
        self._image: Optional[Image] = None
        self._variables: Dict[str, str] = {}
        self._tags: OrderedSetType = {}
        self._rules: List[Rule] = []
        self._needs: List[Union[Need, Job, Sequence]] = []
        self._scripts: List[str]
        self._artifacts: Optional[Artifacts] = None
        self._cache: Optional[Cache] = None
        self._parents: List[Sequence] = list()
        self._original: Optional[Job]
        """Only set if you get a `copy()` of this job"""

        if stage and name:
            self._name = f"{stage}-{name}"
            self._stage = stage
        elif stage:
            self._name = stage
            self._stage = stage
        elif name:
            self._name = name
            # default for unset stages is 'test' -> https://docs.gitlab.com/ee/ci/yaml/#stages
            self._stage = "test"
        else:
            raise ValueError("At least one of the parameters `name` or `stage` have to be set.")

        self._name = self._name.replace("_", "-")
        self._stage = self._stage.replace("-", "_")

        if isinstance(script, str):
            self._scripts = [script]
        elif isinstance(script, list):
            self._scripts = script
        else:
            raise AttributeError("script parameter must be of type string or list of strings")

    @property
    def name(self) -> str:
        """The name of the Job

        This property is affected by the rendering process, where `gcip.core.sequence.Sequence`s will
        populate the job name depending on their names. That means you can be sure to get the jobs
        final name when rendered.
        """
        return self._name

    @property
    def stage(self) -> str:
        """The [stage](https://docs.gitlab.com/ee/ci/yaml/README.html#stage) of the Job

        This property is affected by the rendering process, where `gcip.core.sequence.Sequence`s will
        populate the job stage depending on their stages. That means you can be sure to get the jobs
        final stage when rendered.
        """
        return self._stage

    @property
    def image(self) -> Optional[Image]:
        """The [image](https://docs.gitlab.com/ee/ci/yaml/README.html#image) of the Job"""
        return self._image

    @property
    def variables(self) -> Dict[str, str]:
        """The [variables](https://docs.gitlab.com/ee/ci/yaml/README.html#variables) of the Job"""
        return self._variables

    @property
    def tags(self) -> OrderedSetType:
        """The [tags](https://docs.gitlab.com/ee/ci/yaml/README.html#tags) of the Job"""
        return self._tags

    @property
    def rules(self) -> List[Rule]:
        """The [rules](https://docs.gitlab.com/ee/ci/yaml/README.html#rules) of the Job"""
        return self._rules

    @property
    def needs(self) -> List[Union[Need, Job, Sequence]]:
        """The [needs](https://docs.gitlab.com/ee/ci/yaml/README.html#needs) of the Job"""
        return self._needs

    @property
    def scripts(self) -> List[str]:
        """The [script](https://docs.gitlab.com/ee/ci/yaml/README.html#script) of the Job"""
        return self._scripts

    @property
    def cache(self) -> Optional[Cache]:
        """The [cache](https://docs.gitlab.com/ee/ci/yaml/README.html#cache) of the Job"""
        return self._cache

    @property
    def artifacts(self) -> Artifacts:
        """The [artifacts](https://docs.gitlab.com/ee/ci/yaml/README.html#artifacts) of the Job."""
        if not self._artifacts:
            self._artifacts = Artifacts()
        return self._artifacts

    def _extend_name(self, name: Optional[str]) -> None:
        """This method is used by `gcip.core.sequence.Sequence`s to populate the jobs name."""
        if name:
            self._name += "-" + name.replace("_", "-")

    def _extend_stage_value(self, stage: Optional[str]) -> None:
        """This method is used by `gcip.core.sequence.Sequence`s to populate the jobs stage."""
        if stage:
            self._stage += "_" + stage.replace("-", "_")

    def _extend_stage(self, stage: Optional[str]) -> None:
        """This method is used by `gcip.core.sequence.Sequence`s to populate the jobs name and stage."""
        if stage:
            self._extend_name(stage)
            self._extend_stage_value(stage)

    def _add_parent(self, parent: Sequence) -> None:
        """This method is called by `gcip.core.sequence.Sequence`s when the job is added to that sequence.

        The job needs to know its parents when `_get_all_instance_names()` is called.
        """
        self._parents.append(parent)

    def prepend_scripts(self, *scripts: str) -> Job:
        """Inserts one or more [script](https://docs.gitlab.com/ee/ci/yaml/README.html#script)s before the current scripts.

        Returns:
            `Job`: The modified `Job` object.
        """
        self._scripts = list(scripts) + self._scripts
        return self

    def append_scripts(self, *scripts: str) -> Job:
        """Adds one or more [script](https://docs.gitlab.com/ee/ci/yaml/README.html#script)s after the current scripts.

        Returns:
            `Job`: The modified `Job` object.
        """
        self._scripts.extend(scripts)
        return self

    def add_variables(self, **variables: str) -> Job:
        """Adds one or more [variables](https://docs.gitlab.com/ee/ci/yaml/README.html#variables), each as keyword argument,
        to the job.

        Args:
            **variables (str): Each variable would be provided as keyword argument:
        ```
        job.add_variables(GREETING="hello", LANGUAGE="python")
        ```

        Returns:
            `Job`: The modified `Job` object.
        """
        self._variables.update(variables)
        return self

    def add_tags(self, *tags: str) -> Job:
        """Adds one or more [tags](https://docs.gitlab.com/ee/ci/yaml/README.html#tags) to the job.

        Returns:
            `Job`: The modified `Job` object.
        """
        for tag in tags:
            self._tags[tag] = None
        return self

    def set_cache(self, cache: Optional[Cache]) -> Job:
        """Sets the [cache](https://docs.gitlab.com/ee/ci/yaml/README.html#cache) of the Job.

        Any previous values will be overwritten.

        Args:
            cache (Optional[Cache]): See `gcip.core.cache.Cache` class.

        Returns:
            Sequence: Returns the modified `Job` object.
        """
        if cache:
            self._cache = cache
        return self

    def set_artifacts(self, artifacts: Optional[Artifacts]) -> Job:
        """Sets the [artifacts](https://docs.gitlab.com/ee/ci/yaml/README.html#artifacts) of the Job.

        Any previous values will be overwritten.

        Args:
            artifacts: (Artifacts): See `gcip.core.artifacts.Artifacts` class.

        Returns:
            Sequence: Returns the modified `Job` object.
        """
        self._artifact = artifacts
        return self

    def append_rules(self, *rules: Rule) -> Job:
        """Adds one or more  [rule](https://docs.gitlab.com/ee/ci/yaml/README.html#rules)s behind the current rules of the job.

        Args:
            *rules (Rule): See `gcip.core.rule.Rule` class.

        Returns:
            Sequence: Returns the modified `Job` object.
        """
        self._rules.extend(rules)
        return self

    def prepend_rules(self, *rules: Rule) -> Job:
        """Inserts one or more  [rule](https://docs.gitlab.com/ee/ci/yaml/README.html#rules)s before the current rules of the job.

        Args:
            *rules (Rule): See `gcip.core.rule.Rule` class.

        Returns:
            Sequence: Returns the modified `Job` object.
        """
        self._rules = list(rules) + self._rules
        return self

    def add_needs(self, *needs: Union[Need, Job, Sequence]) -> Job:
        """Add one or more [needs](https://docs.gitlab.com/ee/ci/yaml/README.html#needs) to the job.

        Args:
            *needs (Union[Need, Job, Sequence]):

        Returns:
            Sequence: Returns the modified `Job` object.
        """
        self._needs.extend(needs)
        return self

    def set_image(self, image: Optional[Union[Image, str]]) -> Job:
        """Sets the image of this job.

        For a simple container image you can provide the origin of the image.
        If you want to set the entrypoint, you have to provide an Image object instead.

        Args:
            image (Optional[Union[Image, str]]): Can be either `string` or `Image`.

        Returns:
            Job: Returns the modified :class:`Job` object.
        """
        if image:
            if isinstance(image, str):
                image = Image(image)
            self._image = image
        return self

    def _get_all_instance_names(self) -> Set[str]:
        """Query all the possible names this job can have by residing within parent `gcip.core.sequence.Sequence`s.

        The possible image names are built by the `name` of this job plus all the possible prefix values from
        parent parent `gcip.core.sequence.Sequence`s. The prefix values from parent sequences are their names
        prefixed with the names of the parent parent sequences and so on.

        Imagine Job `A` resides within following sequenes:

        ```
        B:
          A
        C:
          D:
            A
        ```

        Then the instance names of `A` would be `A-B` and `A-D-C`.
        """
        instance_names: Set[str] = set()
        for parent in self._parents:
            for postfix in parent._get_all_instance_names(self):
                if postfix:
                    instance_names.add(f"{self._name}-{postfix}")
                else:
                    instance_names.add(self._name)
        return instance_names

    def copy(self) -> Job:
        """Returns an independent, deep copy object of this job.

        Returns:
            `Job`: A copy of this job which, when modified, has no effects on this source job.
        """
        job_copy = copy.deepcopy(self)
        job_copy._original = self
        return job_copy

    def render(self) -> Dict[str, Any]:
        """Return a representation of this Job object as dictionary with static values.

        The rendered representation is used by the gcip to dump it
        in YAML format as part of the .gitlab-ci.yml pipeline.

        Returns:
            Dict[str, Any]: A dictionary representing the job object in Gitlab CI.
        """
        # late import to avoid circular dependencies
        from .sequence import Sequence

        rendered_job: Dict[str, Any] = {}

        if self._image:
            rendered_job.update({"image": self._image.render()})

        if self._needs:
            need_jobs: List[Job] = list()
            rendered_needs: List[Dict[str, Union[str, bool]]] = list()
            for need in self._needs:
                if isinstance(need, Job):
                    need_jobs.append(need)
                elif isinstance(need, Sequence):
                    for job in need.last_jobs_executed:
                        need_jobs.append(job)
                elif isinstance(need, Need):
                    rendered_needs.append(need.render())
                else:
                    raise TypeError(f"Need '{need}' is of type {type(need)}.")

            job_names: Set[str] = set()
            for job in need_jobs:
                job_names.update(job._get_all_instance_names())

            for name in job_names:
                rendered_needs.append(Need(name).render())

            # sort needs by the name of the referenced job
            rendered_needs = sorted(rendered_needs, key=itemgetter("job"))

            rendered_job.update({"needs": rendered_needs})

        rendered_job.update(
            {
                "stage": self._stage,
                "script": self._scripts,
            }
        )

        if self._variables:
            rendered_job["variables"] = self._variables

        if self._rules:
            rendered_rules = []
            for rule in self._rules:
                rendered_rules.append(rule.render())
            rendered_job.update({"rules": rendered_rules})

        if self._cache:
            rendered_job.update({"cache": self._cache.render()})

        if self._artifacts:
            rendered_artifacts = self._artifacts.render()
            if rendered_artifacts:
                rendered_job.update({"artifacts": rendered_artifacts})

        if self._tags.keys():
            rendered_job["tags"] = list(self._tags.keys())

        return rendered_job


class TriggerStrategy(Enum):
    """This class represents the [trigger:strategy](https://docs.gitlab.com/ee/ci/yaml/README.html#linking-pipelines-with-triggerstrategy)
    keyword."""

    DEPEND = "depend"
    """Use this strategy to force the `TriggerJob` to wait for the downstream (multi-project or child) pipeline to complete."""


class TriggerJob(Job):
    """This class represents the [trigger](https://docs.gitlab.com/ee/ci/yaml/README.html#trigger) job.

    Jobs with trigger can only use a [limited set of keywords](https://docs.gitlab.com/ee/ci/multi_project_pipelines.html#limitations).
    For example, you can’t run commands with `script`.

    Simple example:

    ```python
    trigger_job = TriggerJob(
        stage="trigger-other-job",
        project="myteam/other-project",
        branch="main",
        strategy=TriggerStrategy.DEPEND,
    )
    trigger_job.append_rules(rules.on_tags().never(), rules.on_main())
    ```

    Args:
        project (Optional[str]): The full name of another Gitlab project to trigger (multi-project pipeline trigger)
            Mutually exclusive with `includes`. Defaults to None.
        branch (Optional[str]): The branch of `project` the pipeline should be triggered of. Defaults to None.
        includes (Optional[List[Include]]): Include a pipeline to trigger (Parent-child pipeline trigger)
            Mutually exclusiv with `project`. Defaults to None.
        strategy (Optional[TriggerStrategy]): Determines if the result of this pipeline depends on the triggered downstream pipeline
            (use `TriggerStrategy.DEPEND`) or if just "fire and forget" the downstream pipeline (use `None`). Defaults to None.

    Raises:
        ValueError: If both `project` and `includes` are given.
        ValueError: When the limit of three child pipelines is exceeded. See https://docs.gitlab.com/ee/ci/parent_child_pipelines.html
            for more information.
    """

    def __init__(
        self,
        *args: Any,
        name: Optional[str] = None,
        stage: Optional[str] = None,
        project: Optional[str] = None,
        branch: Optional[str] = None,
        includes: Union[Include, List[Include], None] = None,
        strategy: Optional[TriggerStrategy] = None,
        **kwargs: Mapping[Any, Any],
    ) -> None:

        if includes and project:
            raise ValueError(("You cannot specify 'include' and 'project' together. Either 'include' or 'project' is possible."))
        if not includes and not project:
            raise ValueError("Neither 'includes' nor 'project' is given.")

        super().__init__(name=name, stage=stage, script="none")

        self._project = project
        self._branch = branch
        self._strategy = strategy

        if not includes:
            self._includes = None
        elif isinstance(includes, Include):
            self._includes = [includes]
        elif isinstance(includes, list):
            if len(includes) > 3:
                raise ValueError(
                    ("The length of 'includes' is limited to three." "See https://docs.gitlab.com/ee/ci/parent_child_pipelines.html for more information.")
                )
            self._includes = includes
        else:
            raise AttributeError("script parameter must be of type string or list of strings")

    def render(self) -> Dict[Any, Any]:
        """Return a representation of this TriggerJob object as dictionary with static values.

        The rendered representation is used by the gcip to dump it
        in YAML format as part of the .gitlab-ci.yml pipeline.

        Returns:
            Dict[str, Any]: A dictionary representing the trigger job object in Gitlab CI.
        """
        rendered_job = super().render()

        # remove unsupported keywords from TriggerJob
        rendered_job.pop("script")

        if "image" in rendered_job:
            rendered_job.pop("image")

        if "tags" in rendered_job:
            rendered_job.pop("tags")

        if "artifacts" in rendered_job:
            rendered_job.pop("artifacts")

        if "cache" in rendered_job:
            rendered_job.pop("cache")

        trigger: Dict[str, Union[str, List[Dict[str, str]]]] = {}

        # Child pipelines
        if self._includes:
            trigger.update(
                {
                    "include": [include.render() for include in self._includes],
                }
            )

        # Multiproject pipelines
        if self._project:
            trigger.update(
                {
                    "project": self._project,
                }
            )
            if self._branch:
                trigger.update({"branch": self._branch})

        if self._strategy:
            trigger.update({"strategy": self._strategy.value})

        rendered_job = {"trigger": trigger, **rendered_job}

        return rendered_job
