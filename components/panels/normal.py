from pathlib import Path

from libqtile import widget, bar, qtile
from libqtile.config import Screen

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

widgets_list = [
    spacer,
    workspaces,
    powerline_left,
    widget.Spacer(),
    powerline_right,
    clock,
    powerline_left,
    widget.Spacer(),
    hidden_systray,
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
            size=28,
            opacity=1,
            background=theme.background,
            border_width=3,
            border_color=theme.contrast[0][0],
            margin=[9, 9, 0, 9],
        )
    ),
]
