from djura.entities.project import Project
from djura.entities.tool import Tool


class Poetry(Tool):
    @staticmethod
    def get_required_instances(project: Project) -> frozenset["Poetry"]:
        if "poetry.lock" in project.files:
            return frozenset({Poetry()})
        else:
            return frozenset()
