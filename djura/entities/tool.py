from abc import ABC, abstractmethod

from djura.entities.project import Project


class Tool(ABC):
    @staticmethod
    @abstractmethod
    def get_required_instances(project: Project) -> frozenset["Tool"]:
        ...
