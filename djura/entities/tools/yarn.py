from __future__ import annotations

from djura.entities.filename import Filename
from djura.entities.project import Project
from djura.entities.tool import Tool
from djura.entities.version import Version


class Yarn(Tool):
    @staticmethod
    def get_required_instances(project: Project) -> frozenset[Yarn]:
        if Filename("yarn.lock") in project.files:
            return frozenset({Yarn()})
        else:
            return frozenset()

    def does_version_fit(self, version: Version) -> bool:
        return True
