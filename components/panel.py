from libqtile import widget, bar, qtile
from libqtile.config import Screen

from themes.themes import theme
from constants import HOME, TERMINAL

widget_defaults = dict(
    font="JetBrainsMono Nerd Font Bold",
    # font="OpenDyslexic Nerd Font",
    # font="CaskaydiaCove Nerd Font",
    # font="ProggyCleanTTSZ Nerd Font",
    # font="TerminessTTF Nerd Font",
    fontsize=15,
    padding=2,
    background=theme.background,
    foreground=theme.foreground,
)


def init_powerline_widget(
    foreground: list[str] = theme.foreground,
    background: list[str] = theme.background,
    # text="",
    text=" ",
    # text="",
) -> widget.TextBox:
    """
    Creates a template widget to create the powerline effect implementation.
    """
    return widget.TextBox(
        text=text,
        padding=0,
        foreground=foreground,
        background=background,
        fontsize=20,
    )


fg_spacer = widget.Spacer(
    length=9,
    background=theme.accent,
)
bg_spacer = widget.Spacer(
    length=7,
)
group_box = widget.GroupBox(
    fontsize=25,
    borderwidth=3,
    active=theme.foreground,
    inactive=theme.contrast[0],
    rounded=False,
    highlight_method="text",
    urgent_alert_method="text",
    this_current_screen_border=theme.accent,
    disable_drag=True,
)
hidden_task_list = widget.WidgetBox(
    widgets=[
        widget.TaskList(
            highlight_method="border",
            borderwidth=1,
            icon_size=17,
            max_title_width=150,
            rounded=True,
            padding=1,
            border=theme.accent,
            margin=0,
            txt_floating="🗗",
            txt_minimized=">_ ",
        ),
    ],
    text_closed=" ",
    text_open=" ",
    foreground=theme.accent,
)
current_layout = [
    widget.CurrentLayoutIcon(
        background=theme.accent,
        custom_icon_paths=[f"{HOME}/.config/qtile/icons"],
        padding=0,
        scale=0.7,
    ),
    widget.CurrentLayout(
        background=theme.accent,
    ),
]
check_updates = widget.CheckUpdates(
    background=theme.accent,
    display_format=" {updates}",
    no_update_string=" 0",
    mouse_callbacks={
        "Button1": lambda: qtile.cmd_spawn(f"{TERMINAL} -e sudo pacman -Syu")
    },
    distro="Arch",
)
hidden_net = widget.WidgetBox(
    widgets=[
        widget.Net(
            # interface=["wlp6s0"],
            interface=["wlp1s0"],
            format="{down} 祝{up}",
            padding=0,
            foreground=theme.accent,
        )
    ],
    text_closed=" ",
    text_open=" : ",
    foreground=theme.accent,
)
hidden_pc_status = widget.WidgetBox(
    widgets=[
        widget.DF(
            foreground=theme.accent,
            visible_on_warn=False,
            format=" {uf}G {r:.0f}% ",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(f"{TERMINAL} -e htop")
            },
        ),
        widget.CPU(
            foreground=theme.accent,
            update_interval=1,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(f"{TERMINAL} -e htop")
            },
            format=" {freq_current}GHz {load_percent}% ",
        ),
        widget.Memory(
            foreground=theme.accent,
            format=" {MemUsed:.0f}M/{MemTotal:.0f}M",
            update_interval=1,
            measure_mem="M",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(f"{TERMINAL} -e htop")
            },
        ),
    ],
    text_closed="",
    text_open=": ",
    foreground=theme.accent,
)
clock = widget.Clock(
    background=theme.accent,
    format=" %d/%m/%Y  %H:%M",
)
hidden_systray = widget.WidgetBox(
    widgets=[
        widget.Systray(
            icon_size=20,
            padding=4,
        ),
    ],
    foreground=theme.accent,
    text_closed="  ",
    text_open=" ",
)
battery = widget.Battery(
    foreground=theme.accent,
    format="{char} {percent:2.0%}",
    charge_char=" ",
    discharge_char="",
    full_char="",
    unknown_char="",
    empty_char="",
    low_percentage=0.2,
    low_foreground=theme.alert,
)
python_logo = widget.TextBox(
    text=" ",
    fontsize=20,
    background=theme.accent,
    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show drun")},
)
right_separator_bg = init_powerline_widget(
    background=theme.accent,
    foreground=theme.background,
)
right_separator_fg = init_powerline_widget(
    foreground=theme.accent,
    background=theme.background,
)
left_separator_bg = init_powerline_widget(
    text=" ",
    background=theme.accent,
    foreground=theme.background,
)
left_separator_fg = init_powerline_widget(
    text=" ",
    foreground=theme.accent,
    background=theme.background,
)

widgets_list = [
    fg_spacer,
    python_logo,
    left_separator_fg,
    group_box,
    left_separator_bg,
    *current_layout,
    left_separator_fg,
    hidden_task_list,
    widget.Spacer(),
    hidden_systray,
    hidden_pc_status,
    right_separator_fg,
    check_updates,
    right_separator_bg,
    hidden_net,
    right_separator_fg,
    clock,
    right_separator_bg,
    battery,
    bg_spacer,
]

screens = [
    Screen(
        top=bar.Bar(
            widgets=widgets_list,
            size=25,
            opacity=1,
            background="000000",
            margin=[9, 9, 0, 9],
        )
    ),
]
