from dataclasses import dataclass

from djura.entities.file import File


@dataclass
class TextFile(File):
    text: str
