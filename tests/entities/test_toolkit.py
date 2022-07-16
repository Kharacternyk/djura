from modulefinder import ModuleFinder
from pathlib import Path
from pkgutil import iter_modules

DJURA_ENTITIES_PATH = Path(__file__).parent.parent.with_name("djura") / "entities"
TOOKIT_MODULE_PATH, TOOLS_MODULES_PATH = (
    str((DJURA_ENTITIES_PATH / filename).resolve())
    for filename in ("toolkit.py", "tools")
)


def test_toolkit_imports_all_tools():
    finder = ModuleFinder()
    finder.run_script(TOOKIT_MODULE_PATH)
    tools_modules = set(
        f"djura.entities.tools.{module.name}"
        for module in iter_modules([TOOLS_MODULES_PATH])
    )
    assert tools_modules
    assert not tools_modules.difference(finder.modules.keys())
