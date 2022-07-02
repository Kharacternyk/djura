from dataclasses import dataclass

from djura.entities.file import File


@dataclass(frozen=True)
class Directory(File):
    files: frozenset[File]
