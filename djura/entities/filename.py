from dataclasses import dataclass


@dataclass(frozen=True)
class Filename:
    value: str
