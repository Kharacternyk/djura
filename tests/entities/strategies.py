from hypothesis.strategies import characters, composite, dictionaries, text

from djura.entities.file import File
from djura.entities.filename import Filename
from djura.entities.project import Project


@composite
def filenames(draw):
    return Filename(draw(text(characters(blacklist_characters="/"))))


@composite
def files(draw):
    return File(draw(text()))


@composite
def projects(draw):
    return Project(draw(dictionaries(filenames(), files())))
