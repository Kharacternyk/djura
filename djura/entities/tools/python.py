from dataclasses import dataclass
from typing import cast

import tomli
from poetry.core.semver import Version as PoetryVersion
from poetry.core.semver import VersionTypes, parse_constraint
from typing_extensions import Self

from djura.entities.filename import Filename
from djura.entities.project import Project
from djura.entities.tool import Tool
from djura.entities.version import Version


@dataclass(frozen=True)
class Python(Tool):
    _poetry_version: VersionTypes | None

    @classmethod
    def get_required_instances(cls, project: Project) -> frozenset[Self]:
        pyproject = project.files.get(Filename("pyproject.toml"))
        if not pyproject:
            return frozenset()
        try:
            data = tomli.loads(pyproject.text)
            version_pattern = data["tool"]["poetry"]["dependencies"]["python"]
        except (tomli.TOMLDecodeError, KeyError):
            return frozenset()
        return frozenset({Python(parse_constraint(version_pattern))})

    def does_version_fit(self, version: Version) -> bool:
        if not self._poetry_version:
            return False
        try:
            poetryVersion = PoetryVersion.parse(version.text)
        except ValueError:
            return False
        return cast(bool, self._poetry_version.allows(poetryVersion))
