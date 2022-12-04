from libqtile import widget, bar, qtile
from libqtile.config import Screen

from colors import colors
from components import HOME, TERMINAL


widget_defaults = dict(
    font="JetBrainsMono Nerd Font Bold",
    fontsize=15,
    padding=2,
    background=colors.primary.background,
    foreground=colors.primary.foreground,
)


def init_powerline_widget(
    foreground: list[str] = colors.primary.foreground,
    background: list[str] = colors.primary.background,
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
    background=colors.normal.blue,
)
bg_spacer = widget.Spacer(
    length=7,
)
group_box = widget.GroupBox(
    fontsize=40,
    borderwidth=3,
    active=colors.primary.foreground,
    inactive=colors.primary.background_light,
    rounded=False,
    highlight_method="text",
    urgent_alert_method="text",
    this_current_screen_border=colors.normal.blue,
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
            border=colors.normal.blue,
            margin=0,
            txt_floating="🗗",
            txt_minimized=">_ ",
        ),
    ],
    text_closed=" ",
    text_open=" ",
    foreground=colors.normal.blue,
)
current_layout = [
    widget.CurrentLayoutIcon(
        background=colors.normal.blue,
        custom_icon_paths=[f"{HOME}/.config/qtile/icons"],
        padding=0,
        scale=0.7,
    ),
    widget.CurrentLayout(
        background=colors.normal.blue,
    ),
]
check_updates = widget.CheckUpdates(
    background=colors.normal.blue,
    display_format=" {updates}",
    no_update_string=" 0",
    mouse_callbacks={
        "Button1": lambda: qtile.cmd_spawn(f"{TERMINAL} -e sudo pacman -Syu")
    },
    # distro="Garuda",
    distro="Arch",
)
hidden_net = widget.WidgetBox(
    widgets=[
        widget.Net(
            # interface=["wlp6s0"],
            interface=["wlp1s0"],
            format="{down} 祝{up}",
            padding=0,
            foreground=colors.normal.blue,
        )
    ],
    text_closed=" ",
    text_open=" : ",
    foreground=colors.normal.blue,
)
hidden_pc_status = widget.WidgetBox(
    widgets=[
        widget.DF(
            foreground=colors.normal.blue,
            visible_on_warn=False,
            format=" {uf}G {r:.0f}% ",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(f"{TERMINAL} -e htop")},
        ),
        widget.CPU(
            foreground=colors.normal.blue,
            update_interval=1,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(f"{TERMINAL} -e htop")},
            format=" {freq_current}GHz {load_percent}% ",
        ),
        widget.Memory(
            foreground=colors.normal.blue,
            format=" {MemUsed:.0f}M/{MemTotal:.0f}M",
            update_interval=1,
            measure_mem="M",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(f"{TERMINAL} -e htop")},
        ),
    ],
    text_closed="",
    text_open=": ",
    foreground=colors.normal.blue,
)
clock = widget.Clock(
    background=colors.normal.blue,
    format=" %d/%m/%Y  %H:%M",
)
hidden_systray = widget.WidgetBox(
    widgets=[
        widget.Systray(
            icon_size=20,
            padding=4,
        ),
    ],
    foreground=colors.normal.blue,
    text_closed="  ",
    text_open=" ",
)
battery = widget.Battery(
    foreground=colors.normal.blue,
    format="{char} {percent:2.0%}",
    charge_char=" ",
    discharge_char="",
    full_char="",
    unknown_char="",
    empty_char="",
    low_percentage=0.2,
    low_foreground=colors.bright.red,
)
python_logo = widget.TextBox(
    text=" ",
    fontsize=20,
    background=colors.normal.blue,
    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show drun")},
)
right_separator_bg = init_powerline_widget(
    background=colors.normal.blue,
    foreground=colors.primary.background,
)
right_separator_fg = init_powerline_widget(
    foreground=colors.normal.blue,
    background=colors.primary.background,
)
left_separator_bg = init_powerline_widget(
    text=" ",
    background=colors.normal.blue,
    foreground=colors.primary.background,
)
left_separator_fg = init_powerline_widget(
    text=" ",
    foreground=colors.normal.blue,
    background=colors.primary.background,
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
