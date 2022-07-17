from dataclasses import dataclass
from typing import Iterable, Type

from typing_extensions import Self

from djura.entities.project import Project
from djura.entities.tool import Tool
from djura.entities.tools.poetry import Poetry
from djura.entities.tools.python import Python
from djura.entities.tools.sam_cli import SamCli
from djura.entities.tools.yarn import Yarn

TOOL_CLASSES: Iterable[Type[Tool]] = {
    Poetry,
    Python,
    SamCli,
    Yarn,
}


@dataclass(frozen=True)
class Toolkit:
    tools: frozenset[Tool]

    @classmethod
    def from_project(cls, project: Project) -> Self:
        tools: set[Tool] = set()
        for toolClass in TOOL_CLASSES:
            tools.update(toolClass.get_required_instances(project))
        return Toolkit(frozenset(tools))
