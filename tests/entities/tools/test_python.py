import pytest

from djura.entities.file import File
from djura.entities.filename import Filename
from djura.entities.project import Project
from djura.entities.tools.python import Python
from djura.entities.version import Version


@pytest.mark.parametrize(
    ("pattern", "version", "does_fit"),
    [
        ("~3.7", "3.7.0", True),
        ("^3.7", "3.11.5", True),
        (">=3.8.2, <3.11.1", "3.11.0", True),
        ("~3.7", "3.8.0", False),
        ("^3.7", "3.6.5", False),
        (">=3.8.2, <3.11.1", "3.11.1", False),
    ],
)
def test_poetry_version_patterns_are_correctly_parsed(pattern, version, does_fit):
    project = Project(
        {
            Filename("pyproject.toml"): File(
                f'[tool.poetry.dependencies]\npython = "{pattern}"'
            )
        }
    )
    pythons = Python.get_required_instances(project)

    assert len(pythons) == 1

    python = next(iter(pythons))

    assert python.does_version_fit(Version(version)) == does_fit
