from hypothesis.strategies import (
    booleans,
    characters,
    composite,
    frozensets,
    sampled_from,
    text,
)

from djura.entities.directory import Directory
from djura.entities.file import File
from djura.entities.project import Project

_file_names = text(characters(blacklist_characters="/"))
_special_files = ["poetry.lock"]


@composite
def directories(draw):
    return Directory(draw(_file_names), draw(frozensets(files())))


@composite
def files(draw):
    if draw(booleans()):
        return draw(directories())
    if draw(booleans()):
        return File(draw(sampled_from(_special_files)))
    return File(draw(_file_names))


@composite
def projects(draw):
    return Project(draw(directories()))
