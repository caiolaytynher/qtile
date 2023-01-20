from pathlib import Path

from libqtile import widget, bar, qtile
from libqtile.config import Screen

from constants import TERMINAL
from themes.themes import theme

widget_defaults = {
    "font": "JetBrainsMono Nerd Font Bold",
    "fontsize": 14,
    "padding": 5,
    "background": theme.background,
    "foreground": theme.foreground,
}

spacer = widget.Spacer(
    length=15,
    background=theme.contrast[0],
)

powerline_defaults = {
    "foreground": theme.contrast[0],
    "padding": 0,
    "fontsize": 29,
}

powerline_left = widget.TextBox(
    text="\ue0b8 ",
    **powerline_defaults,
)

powerline_right = widget.TextBox(
    text="\ue0be ",
    **powerline_defaults,
)

powerline_sep = widget.TextBox(
    text="\ue0b9 ",
    **powerline_defaults,
)

workspaces = widget.GroupBox(
    fontsize=25,
    borderwidth=3,
    highlight_method="text",
    urgent_alert_method="text",
    background=theme.contrast[0],
    this_current_screen_border=theme.foreground,
    active=theme.contrast[2],
    inactive=theme.contrast[0],
    disable_drag=True,
    rounded=False,
    hide_unused=True,
)

current_layout = widget.CurrentLayoutIcon(
    custom_icon_paths=[str(Path.home() / ".config/qtile/icons")],
    scale=0.5,
    background=theme.contrast[0],
    foreground=theme.foreground,
    padding=0,
)

clock = widget.Clock(
    format="\uf5f5 %b, %d \uf017 %H:%M",
    background=theme.contrast[0],
)

hidden_systray = widget.WidgetBox(
    widgets=[
        widget.Systray(
            icon_size=17,
            padding=8,
        ),
    ],
    text_closed="\uf0d7",
    text_open="\uf0da ",
)

battery = widget.Battery(
    format="\uf578{char} {percent:2.0%}",
    charge_char="\U000f140b",
    discharge_char="",
    full_char="\uf00c",
    unknown_char="\uf128",
    empty_char="\uf12a",
    low_percentage=0.2,
    low_foreground=theme.alert,
)

temperature = widget.ThermalSensor(
    foreground=theme.foreground,
    padding=10,
    format="\uf2c9 {temp:.0f}{unit}",
)

disk_free_space = widget.DF(
    visible_on_warn=False,
    format="\uf98a {uf}G, {r:.0f}% ",
)

cpu_usage = widget.CPU(
    update_interval=1,
    format="\uf85a {freq_current}GHz, {load_percent}% ",
)

ram_usage = widget.Memory(
    format="\ue266 {MemUsed:.0f}M/{MemTotal:.0f}M",
    update_interval=1,
    measure_mem="M",
)


windows_open = widget.TaskList(
    highlight_method="block",
    icon_size=17,
    max_title_width=150,
    rounded=False,
    padding=4,
    border=theme.contrast[0],
    margin=0,
    txt_floating="\uf2d2 ",
    txt_minimized="\uf2d1 ",
    txt_maximized="\uf2d0 ",
)

widgets_list = [
    spacer,
    workspaces,
    powerline_left,
    windows_open,
    widget.Spacer(),
    powerline_right,
    clock,
    powerline_left,
    widget.Spacer(),
    hidden_systray,
    powerline_sep,
    temperature,
    disk_free_space,
    cpu_usage,
    ram_usage,
    powerline_sep,
    battery,
    powerline_right,
    current_layout,
    spacer,
]

screens = [
    Screen(
        top=bar.Bar(
            widgets=widgets_list,
            size=25,
            opacity=1,
            background=theme.background,
        )
    ),
]
