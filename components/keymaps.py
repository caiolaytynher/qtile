import os

from libqtile.command import lazy
from libqtile.config import EzKey, EzDrag, EzClick

HOME = os.path.expanduser("~")
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

window_navigation = [
    EzKey("M-k", lazy.layout.up()),
    EzKey("M-j", lazy.layout.down()),
    EzKey("M-h", lazy.layout.left()),
    EzKey("M-l", lazy.layout.right()),
    EzKey("M-<Up>", lazy.layout.up()),
    EzKey("M-<Down>", lazy.layout.down()),
    EzKey("M-<Left>", lazy.layout.left()),
    EzKey("M-<Right>", lazy.layout.right()),
]

window_manipulation = [
    EzKey("M-f", lazy.window.toggle_fullscreen()),
    EzKey("M-S-f", lazy.window.toggle_floating()),
    EzKey("M-q", lazy.window.kill()),
    EzKey("M-C-k", lazy.layout.grow_up()),
    EzKey("M-C-j", lazy.layout.grow_down()),
    EzKey("M-C-h", lazy.layout.grow_left()),
    EzKey("M-C-l", lazy.layout.grow_right()),
    EzKey("M-C-<Up>", lazy.layout.grow_up()),
    EzKey("M-C-<Down>", lazy.layout.grow_down()),
    EzKey("M-C-<Left>", lazy.layout.grow_left()),
    EzKey("M-C-<Right>", lazy.layout.grow_right()),
    EzKey("M-S-k", lazy.layout.shuffle_up()),
    EzKey("M-S-j", lazy.layout.shuffle_down()),
    EzKey("M-S-h", lazy.layout.swap_left()),
    EzKey("M-S-l", lazy.layout.swap_right()),
    EzKey("M-S-<Up>", lazy.layout.shuffle_up()),
    EzKey("M-S-<Down>", lazy.layout.shuffle_down()),
    EzKey("M-S-<Left>", lazy.layout.swap_left()),
    EzKey("M-S-<Right>", lazy.layout.swap_right()),
]

layout_control = [
    EzKey("M-n", lazy.layout.normalize()),
    EzKey("M-<space>", lazy.next_layout()),
    EzKey("M-S-<space>", lazy.prev_layout()),
]

desktop_control = [
    EzKey("M-b", lazy.spawn("qtile cmd-obj -o cmd -f hide_show_bar")),
    EzKey("M-S-r", lazy.restart()),
    EzKey("M-S-x", lazy.spawn("power-off-screen")),
    EzKey("M-S-c", lazy.spawn("change-color-scheme")),
    EzKey("M-S-o", lazy.spawn("picom-toggle")),
    EzKey("<Print>", lazy.spawn(f"flameshot full -p {HOME}/Pictures/screenshots")),
]

app_spawn = [
    EzKey("M-<Return>", lazy.spawn(TERMINAL)),
    EzKey("M-<KP_Enter>", lazy.spawn(TERMINAL)),
    EzKey("M-m", lazy.spawn("pcmanfm")),
]

app_launcher_spawn = [
    EzKey("M-p", lazy.spawn("rofi -show drun")),
    EzKey("M-S-d", lazy.spawn("my_dmenu")),
]

multimedia = [
    EzKey("<XF86AudioMute>", lazy.spawn("change-volume mute")),
    EzKey("<XF86AudioLowerVolume>", lazy.spawn("change-volume down")),
    EzKey("<XF86AudioRaiseVolume>", lazy.spawn("change-volume up")),
    EzKey("<XF86AudioPlay>", lazy.spawn("playerctl play-pause")),
    EzKey("<XF86AudioNext>", lazy.spawn("playerctl next")),
    EzKey("<XF86AudioPrev>", lazy.spawn("playerctl previous")),
    EzKey("<XF86AudioStop>", lazy.spawn("playerctl stop")),
]

brightness = [
    EzKey("<XF86MonBrightnessUp>", lazy.spawn("change-brightness up")),
    EzKey("<XF86MonBrightnessDown>", lazy.spawn("change-brightness down")),
]

keys = [
    *window_navigation,
    *window_manipulation,
    *layout_control,
    *desktop_control,
    *app_spawn,
    *app_launcher_spawn,
    *multimedia,
    *brightness,
]
