from abc import ABC, abstractmethod
from enum import Enum, auto

from djura.entities.tool import Tool
from djura.entities.version import Version


class ToolSupplier(ABC):
    @abstractmethod
    def install(self, tool: Tool) -> Version | None:
        ...

    @abstractmethod
    def uninstall(self, tool: Tool, version: Version) -> None:
        ...

    @abstractmethod
    def is_installed(self, tool: Tool) -> bool
        ...
