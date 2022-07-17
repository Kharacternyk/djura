from typing_extensions import Self

from djura.entities.filename import Filename
from djura.entities.project import Project
from djura.entities.tool import Tool
from djura.entities.version import Version


class FilenameTriggeredTool(Tool):
    filename: str

    @classmethod
    def get_required_instances(cls, project: Project) -> frozenset[Self]:
        if Filename(cls.filename) in project.files:
            return frozenset({cls()})
        else:
            return frozenset()

    def does_version_fit(self, version: Version) -> bool:
        return True
