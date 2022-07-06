from hypothesis import given

from djura.entities.toolkit import Toolkit
from tests.entities.strategies import SPECIAL_FILES, projects


@given(projects())
def test_toolkit_is_not_empty_if_there_are_special_files_in_the_project(project):
    toolkit = Toolkit.from_project(project)
    if frozenset(project.files).intersection(SPECIAL_FILES):
        assert toolkit.tools
