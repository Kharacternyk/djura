from dataclasses import dataclass

from djura.entities.directory import Directory


@dataclass(frozen=True)
class Project:
    root: Directory
