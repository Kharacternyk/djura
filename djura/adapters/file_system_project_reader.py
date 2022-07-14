from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator, TypeVar, overload

from djura.entities.file import File
from djura.entities.filename import Filename
from djura.entities.project import Project
from djura.ports.project_reader import ProjectReader, ProjectReadingException

T = TypeVar("T")


@dataclass(frozen=True)
class FileSystemProjectReader(ProjectReader):
    path: Path

    def get_project(self) -> Project:
        return Project(_FilesMapping(self.path))


@dataclass(frozen=True)
class _FilesMapping(Mapping[Filename, File]):
    # TODO: Avoid race conditions.

    root: Path
    cache: dict[Filename, File] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.root.is_dir():
            raise ProjectReadingException(f"{self.root} is not a directory")

    @overload
    def get(self, filename: Filename) -> File | None:
        ...

    @overload
    def get(self, filename: Filename, default: T) -> File | T:
        ...

    def get(
        self, filename: Filename, default: File | T | None = None
    ) -> File | T | None:
        if filename not in self.cache:
            path = self.to_path(filename)
            if not path.is_file():
                return default
            else:
                self.cache[filename] = File(path.read_text(errors="backslashreplace"))
        return self.cache[filename]

    def __contains__(self, item: object) -> bool:
        if isinstance(item, Filename):
            return item in self.cache or self.to_path(item).is_file()
        return False

    def __getitem__(self, filename: Filename) -> File:
        file = self.get(filename)
        if not file:
            raise KeyError(filename)
        return file

    def __iter__(self) -> Iterator[Filename]:
        for path in self.root.iterdir():
            if path.is_file():
                yield Filename(path.name)

    def __len__(self) -> int:
        return len(tuple(self))

    def to_path(self, filename: Filename) -> Path:
        return self.root / filename.value
