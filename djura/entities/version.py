from dataclasses import dataclass


@dataclass(frozen=True)
class Version:
    text: str
