from abc import ABC, abstractmethod

from typing_extensions import Self

from djura.entities.project import Project
from djura.entities.version import Version


class Tool(ABC):
    @classmethod
    @abstractmethod
    def get_required_instances(cls, project: Project) -> frozenset[Self]:
        ...

    @abstractmethod
    def does_version_fit(self, version: Version) -> bool:
        ...
