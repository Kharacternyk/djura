from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Type, TypeVar

from djura.entities.project import Project
from djura.entities.version import Version

T = TypeVar("T")


class Tool(ABC):
    @classmethod
    @abstractmethod
    def get_required_instances(cls: Type[T], project: Project) -> frozenset[T]:
        ...

    @abstractmethod
    def does_version_fit(self, version: Version) -> bool:
        ...
