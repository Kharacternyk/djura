from hypothesis import given

from djura.entities.filename import Filename
from djura.entities.tools.poetry import Poetry
from tests.entities.strategies import projects


@given(projects())
def test_poetry_is_required_if_and_only_if_there_is_a_lock_file(project):
    if Filename("poetry.lock") in project.files:
        assert Poetry.get_required_instances(project)
    else:
        assert not Poetry.get_required_instances(project)


@given(projects())
def test_multiple_poetries_are_never_required(project):
    assert len(Poetry.get_required_instances(project)) in (0, 1)
