from dataclasses import dataclass

from djura.entities.project import Project
from djura.entities.tool import Tool
from djura.entities.tools.poetry import Poetry
from djura.entities.tools.python import Python


@dataclass(frozen=True)
class Toolkit:
    tools: frozenset[Tool]

    @staticmethod
    def from_project(project: Project) -> "Toolkit":
        tools: set[Tool] = set()
        for toolClass in (Poetry, Python):
            tools.update(toolClass.get_required_instances(project))  # type: ignore
        return Toolkit(frozenset(tools))
