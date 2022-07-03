from djura.entities.project import Project
from djura.entities.text_file import TextFile
from djura.entities.tool import Tool


class Poetry(Tool):
    @staticmethod
    def get_required_instances(project: Project) -> frozenset["Poetry"]:
        match project.files.get("poetry.lock"):
            case TextFile():
                return frozenset({Poetry()})
            case _:
                return frozenset()
