from hypothesis.strategies import booleans, characters, composite, frozensets, text

from djura.entities.directory import Directory
from djura.entities.file import File
from djura.entities.project import Project

_file_names = text(characters(blacklist_characters="/"))


@composite
def directories(draw):
    return Directory(draw(_file_names), draw(frozensets(files())))


@composite
def files(draw):
    if draw(booleans()):
        return draw(directories())
    return File(draw(_file_names))


@composite
def projects(draw):
    return Project(draw(directories()))
