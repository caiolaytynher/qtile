from .theme import Theme

gruvbox = Theme(
    name="gruvbox",
    background=["#282828", "#282828"],
    contrast=[
        ["#3c3836", "#3c3836"],
        ["#504945", "#504945"],
        ["#665c54", "#665c54"],
        ["#7c6f64", "#7c6f64"],
    ],
    foreground=["#ebdbb2", "#ebdbb2"],
    wallpaper="serenity-1920x1080.jpg",
    accent=["#d65d0e", "#d65d0e"],  # Orange
    alert=["#cc241d", "#cc241d"],
)

dracula = Theme(
    name="dracula",
    background=["#282a36", "#282a36"],
    contrast=[
        ["#343746", "#343746"],
        ["#424450", "#424450"],
        ["#535560", "#535560"],
        ["#63646e", "#63646e"],
    ],
    foreground=["#f8f8f2", "#f8f8f2"],
    wallpaper="blue-landscape.jpg",
    accent=["#bd93f9", "#bd93f9"],  # Blue
    alert=["#ff5555", "#ff5555"],
)

theme = gruvbox
