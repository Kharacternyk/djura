from hypothesis import given

from djura.entities.filename import Filename
from djura.entities.filename_triggered_tool import FilenameTriggeredTool
from tests.entities.strategies import filenames, projects


@given(filenames(), projects())
def test_filename_triggered_tool_is_required_if_and_only_if_there_is_a_special_file(
    special_filename, project
):
    class ConcreteFilenameTriggeredTool(FilenameTriggeredTool):
        filename = special_filename

    instances = ConcreteFilenameTriggeredTool.get_required_instances(project)
    if Filename(special_filename) in project.files:
        assert instances
    else:
        assert not instances


@given(filenames(), projects())
def test_multiple_concrete_filename_triggered_tools_are_never_required(
    special_filename, project
):
    class ConcreteFilenameTriggeredTool(FilenameTriggeredTool):
        filename = special_filename

    instances = ConcreteFilenameTriggeredTool.get_required_instances(project)
    assert len(instances) in (0, 1)
