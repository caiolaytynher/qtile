import os

from libqtile.command import lazy
from libqtile.config import EzKey, EzDrag, EzClick

HOME = os.path.expanduser("~")
SCRIPTS_PATH = f"{HOME}/Documents/scripts"
TERMINAL = "alacritty"

EzKey.modifier_keys = {
    "M": "mod4",
    "A": "mod1",
    "S": "shift",
    "C": "control",
}

mouse = [
    EzDrag(
        "M-<Button1>",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    EzDrag(
        "M-<Button3>",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    EzClick(
        "M-<Button2>",
        lazy.window.bring_to_front(),
    ),
]

window_navigation = []

window_manipulation = [
    EzKey("M-f", lazy.window.toggle_fullscreen()),
    EzKey("M-q", lazy.window.kill()),
]

app_spawn = [
    EzKey("M-<Return>", lazy.spawn(TERMINAL)),
    EzKey("M-<KP_Enter>", lazy.spawn(TERMINAL)),
    EzKey("M-m", lazy.spawn("pcmanfm")),
]

qtilectl = [
    EzKey("M-b", lazy.spawn("qtile cmd-obj -o cmd -f hide_show_bar")),
]

rofi_spawn = [
    EzKey("M-p", lazy.spawn("rofi -show drun")),
]
