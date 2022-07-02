from djura.entities.project import Project
from djura.entities.tool import Tool


class Poetry(Tool):
    @staticmethod
    def get_required_instances(project: Project) -> frozenset["Poetry"]:
        if any(file.name == "poetry.lock" for file in project.root.files):
            return frozenset({Poetry()})
        return frozenset()
