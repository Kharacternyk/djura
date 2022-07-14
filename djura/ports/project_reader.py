from abc import ABC, abstractmethod

from djura.entities.project import Project


class ProjectReader(ABC):
    @abstractmethod
    def get_project(self) -> Project:
        ...


class ProjectReadingException(Exception):
    pass
