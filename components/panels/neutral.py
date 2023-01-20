from pathlib import Path

from libqtile import widget, bar, qtile
from libqtile.config import Screen

widget_defaults = {
    "font": "JetBrainsMono Nerd Font Bold",
    "fontsize": 14,
    "padding": 5,
    "background": "#000000",
    "foreground": "#ffffff",
}

spacer = widget.Spacer(
    length=15,
)

separator = widget.Sep(
    padding=30,
    size_percent=50,
    foreground="#7a7a7a",
)

workspaces = widget.GroupBox(
    fontsize=25,
    borderwidth=3,
    highlight_method="text",
    urgent_alert_method="text",
    background="#000000",
    this_current_screen_border="#ffffff",
    active="#7a7a7a",
    inactive="#7a7a7a",
    disable_drag=True,
    rounded=False,
    hide_unused=True,
)

current_layout = widget.CurrentLayoutIcon(
    custom_icon_paths=[str(Path.home() / ".config/qtile/icons")],
    scale=0.5,
    padding=0,
)

clock = widget.Clock(
    format="\uf5f5 %b, %d \uf017 %H:%M",
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
    low_foreground="#f40000",
)

widgets_list = [
    spacer,
    workspaces,
    widget.Spacer(),
    clock,
    widget.Spacer(),
    hidden_systray,
    separator,
    battery,
    separator,
    current_layout,
    spacer,
]

screens = [
    Screen(
        top=bar.Bar(
            widgets=widgets_list,
            size=25,
            opacity=1,
            background="#000000",
        )
    ),
]
