from hypothesis import given

from djura.entities.file import File
from djura.entities.tools.poetry import Poetry
from tests.entities.strategies import projects


@given(projects())
def test_poetry_is_required_if_and_only_if_there_is_a_lock_file(project):
    if Poetry.get_required_instances(project):
        assert File("poetry.lock") in project.root.files
    else:
        assert File("poetry.lock") not in project.root.files


@given(projects())
def test_multiple_poetries_are_never_required(project):
    assert len(Poetry.get_required_instances(project)) in (0, 1)
