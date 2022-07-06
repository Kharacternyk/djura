from hypothesis.strategies import (
    booleans,
    characters,
    composite,
    dictionaries,
    sampled_from,
    text,
)

from djura.entities.file import File
from djura.entities.filename import Filename
from djura.entities.project import Project

_special_files = tuple(Filename(filename) for filename in ["poetry.lock"])


@composite
def filenames(draw):
    if draw(booleans()):
        return draw(sampled_from(_special_files))
    return Filename(draw(text(characters(blacklist_characters="/"))))


@composite
def files(draw):
    return File(draw(text()))


@composite
def projects(draw):
    return Project(draw(dictionaries(filenames(), files())))
