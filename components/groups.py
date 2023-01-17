from libqtile import layout
from libqtile.command import lazy
from libqtile.config import Group, EzKey, Match

from components.keymaps import keys
from themes.themes import theme

groups: list[Group] = [
    Group(
        name="0",
        label="\uf444",
        layout="floating",
    ),
]

# Insert the rest of the groups backwards
for i in range(9, 0, -1):
    groups.insert(
        0,
        Group(
            name=str(i),
            layout="monadtall",
            label="\uf444",
        ),
    )

for group in groups:
    keys.extend(
        [
            EzKey(f"M-{group.name}", lazy.group[group.name].toscreen()),
            EzKey("M-<Tab>", lazy.screen.next_group()),
            EzKey("M-S-<Tab>", lazy.screen.prev_group()),
            EzKey(
                f"M-S-{group.name}",
                lazy.window.togroup(group.name),
                lazy.group[group.name].toscreen(),
            ),
            EzKey(f"M-C-{group.name}", lazy.window.togroup(group.name)),
        ]
    )

border_theme = {
    "margin": 9,
    "border_width": 2,
    "border_focus": theme.accent,
    "border_normal": theme.contrast[0],
}

layouts = [
    layout.MonadTall(**border_theme),
    layout.MonadWide(**border_theme),
    layout.Matrix(**border_theme),
    layout.Zoomy(**border_theme),
    layout.Max(**border_theme),
    layout.Floating(**border_theme),
]

floating_types = ["notification", "toolbar", "splash", "dialog"]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="Arandr"),
        Match(wm_class="feh"),
        Match(wm_class="Galculator"),
        Match(title="branchdialog"),
        Match(title="Open File"),
        Match(title="pinentry"),
        Match(wm_class="ssh-askpass"),
        Match(wm_class="lxpolkit"),
        Match(wm_class="Lxpolkit"),
        Match(wm_class="yad"),
        Match(wm_class="Yad"),
        Match(wm_class="Cairo-dock"),
        Match(wm_class="cairo-dock"),
    ],
    fullscreen_border_width=0,
    border_width=0,
)
