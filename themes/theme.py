from dataclasses import dataclass


@dataclass
class Theme:
    background: list[str]
    contrast: list[list[str]]  # higher index -> lighter color
    foreground: list[str]
    accent: list[str]
    alert: list[str]
