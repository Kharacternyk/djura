from dataclasses import dataclass
from typing import Mapping

from djura.entities.file import File
from djura.entities.filename import Filename


@dataclass(frozen=True)
class Project:
    files: Mapping[Filename, File]
