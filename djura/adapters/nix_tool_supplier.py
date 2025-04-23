from djura.ports.tool_supplier import ToolSupplier
from djura.entities.tool import Tool
from djura.entities.version import Version

from subprocess import run


class NixToolSupplier(ToolSupplier):
    def install(self, tool: Tool) -> Version | None:

