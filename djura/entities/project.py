from dataclasses import dataclass
from typing import Mapping

from djura.entities.file import File


@dataclass(frozen=True)
class Project:
    files: Mapping[str, File]
