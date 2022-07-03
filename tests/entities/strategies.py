from hypothesis.strategies import (
    booleans,
    characters,
    composite,
    dictionaries,
    frozensets,
    sampled_from,
    text,
)

from djura.entities.directory import Directory
from djura.entities.project import Project
from djura.entities.text_file import TextFile


@composite
def file_names(draw):
    if draw(booleans()):
        special_files = ["poetry.lock"]
        return draw(sampled_from(special_files))
    return draw(text(characters(blacklist_characters="/")))


@composite
def directories(draw):
    return Directory(draw(frozensets(file_names())))


@composite
def text_files(draw):
    return TextFile(draw(text()))


@composite
def files(draw):
    if draw(booleans()):
        return draw(text_files())
    return draw(directories())


@composite
def projects(draw):
    return Project(draw(dictionaries(file_names(), files())))
