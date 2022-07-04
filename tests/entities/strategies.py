from hypothesis.strategies import (
    booleans,
    characters,
    composite,
    dictionaries,
    sampled_from,
    text,
)

from djura.entities.file import File
from djura.entities.project import Project

_special_files = ["poetry.lock"]


@composite
def file_names(draw):
    if draw(booleans()):
        return draw(sampled_from(_special_files))
    return draw(text(characters(blacklist_characters="/")))


@composite
def files(draw):
    return File(draw(text()))


@composite
def projects(draw):
    return Project(draw(dictionaries(file_names(), files())))
