from pathlib import Path

from pytest import raises

from djura.adapters.file_system_project_reader import FileSystemProjectReader
from djura.entities.filename import Filename
from djura.ports.project_reader import ProjectReadingException

TEST_PROJECT = Path(__file__).parent / "test-project"


def test_exception_is_thrown_if_project_root_does_not_exist():
    reader = FileSystemProjectReader(TEST_PROJECT.with_name("no-such-project"))
    with raises(ProjectReadingException):
        reader.get_project()


def test_files_can_be_read_if_project_contains_them():
    reader = FileSystemProjectReader(TEST_PROJECT)
    project = reader.get_project()
    for filename in project.files:
        project.files[filename].text


def test_files_are_read_correctly():
    reader = FileSystemProjectReader(TEST_PROJECT)
    project = reader.get_project()
    for name in ("regular-file", "regular-file-link"):
        assert project.files[Filename(name)].text == "Text content.\n"


def test_directories_are_omitted():
    reader = FileSystemProjectReader(TEST_PROJECT)
    project = reader.get_project()
    for name in ("directory", "directory-link"):
        assert Filename(name) not in project.files


def test_directories_broken_links_are_omitted():
    reader = FileSystemProjectReader(TEST_PROJECT)
    project = reader.get_project()
    assert Filename("broken-link") not in project.files
