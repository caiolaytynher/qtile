from dataclasses import dataclass


@dataclass
class Primary:
    background_darker: list[str]
    background_dark: list[str]
    background: list[str]
    background_light: list[str]
    background_lighter: list[str]
    foreground_darker: list[str]
    foreground_dark: list[str]
    foreground: list[str]
    foreground_light: list[str]
    foreground_lighter: list[str]


@dataclass
class Normal:
    black: list[str]
    red: list[str]
    green: list[str]
    yellow: list[str]
    blue: list[str]
    magenta: list[str]
    cyan: list[str]
    white: list[str]


@dataclass
class Bright:
    black: list[str]
    red: list[str]
    green: list[str]
    yellow: list[str]
    blue: list[str]
    magenta: list[str]
    cyan: list[str]
    white: list[str]


@dataclass
class ColorScheme:
    primary: Primary
    normal: Normal
    bright: Bright
