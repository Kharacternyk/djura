from abc import ABC, abstractmethod

from djura.entities.project import Project
from djura.entities.version import Version


class Tool(ABC):
    @staticmethod
    @abstractmethod
    def get_required_instances(project: Project) -> frozenset["Tool"]:
        ...

    @abstractmethod
    def does_version_fit(self, version: Version) -> bool:
        ...
