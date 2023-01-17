from dataclasses import dataclass


@dataclass
class Theme:
    name: str
    background: list[str]
    contrast: list[list[str]]  # higher index -> lighter color
    foreground: list[str]
    wallpaper: str
    accent: list[str]
    alert: list[str]
