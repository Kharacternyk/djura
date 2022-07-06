from dataclasses import dataclass

from djura.entities.project import Project
from djura.entities.tool import Tool
from djura.entities.tools.poetry import Poetry


@dataclass(frozen=True)
class Toolkit:
    tools: frozenset[Tool]

    @staticmethod
    def from_project(project: Project) -> "Toolkit":
        tools: set[Tool] = set()
        for toolClass in (Poetry,):
            tools.update(toolClass.get_required_instances(project))
        return Toolkit(frozenset(tools))
