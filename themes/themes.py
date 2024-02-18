from .theme import Theme

gruvbox = Theme(
    background=["#282828", "#282828"],
    contrast=[
        ["#3c3836", "#3c3836"],
        ["#504945", "#504945"],
        ["#665c54", "#665c54"],
        ["#7c6f64", "#7c6f64"],
    ],
    foreground=["#ebdbb2", "#ebdbb2"],
    accent=["#d65d0e", "#d65d0e"],  # Orange
    alert=["#cc241d", "#cc241d"],
)

dracula = Theme(
    background=["#282a36", "#282a36"],
    contrast=[
        ["#343746", "#343746"],
        ["#424450", "#424450"],
        ["#535560", "#535560"],
        ["#63646e", "#63646e"],
    ],
    foreground=["#f8f8f2", "#f8f8f2"],
    accent=["#bd93f9", "#bd93f9"],  # Blue
    alert=["#ff5555", "#ff5555"],
)

catppuccin = Theme(
    background=["#1E1E2E", "#1E1E2E"],
    contrast=[
        ["#343547", "#343547"],
        ["#3F4154", "#3F4154"],
        ["#4A4C60", "#4A4C60"],
        ["#767A91", "#767A91"],
    ],
    foreground=["#CDD6F4", "#CDD6F4"],
    accent=["#F5C2E7", "#F5C2E7"],
    alert=["#F38BA8", "#F38BA8"],
)

tokyonight = Theme(
    background=["#24283b", "#24283b"],
    contrast=[
        ["#2E3347", "#2E3347"],
        ["#383D53", "#383D53"],
        ["#4B516A", "#4B516A"],
        ["#727998", "#727998"],
    ],
    foreground=["#c0caf5", "#c0caf5"],
    accent=["#f7768e", "#f7768e"],
    alert=["#f7768e", "#f7768e"],
)

everforest = Theme(
    background=["#2d353b", "#2d353b"],
    contrast=[
        ["#383F42", "#383F42"],
        ["#424849", "#424849"],
        ["#575A57", "#575A57"],
        ["#807E73", "#807E73"],
    ],
    foreground=["#d3c6aa", "#d3c6aa"],
    accent=["#a7c080", "#a7c080"],
    alert=["#e67e80", "#e67e80"],
)

kanagawa = Theme(
    background=["#1f1f28", "#1f1f28"],
    contrast=[
        ["#2B2B32", "#2B2B32"],
        ["#37363B", "#37363B"],
        ["#4F4D4D", "#4F4D4D"],
        ["#7E7B71", "#7E7B71"],
    ],
    foreground=["#dcd7ba", "#dcd7ba"],
    accent=["#7e9cd8", "#7e9cd8"],
    alert=["#c34043", "#c34043"],
)

onedark = Theme(
    background=["#1e2127", "#1e2127"],
    contrast=[
        ["#272B31", "#272B31"],
        ["#30343A", "#30343A"],
        ["#42464D", "#42464D"],
        ["#656A73", "#656A73"],
    ],
    foreground=["#abb2bf", "#abb2bf"],
    accent=["#e06c75", "#e06c75"],
    alert=["#e06c75", "#e06c75"],
)

theme = onedark
