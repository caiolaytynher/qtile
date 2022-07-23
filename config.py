from components import hooks, USER, HOSTNAME
from components.groups import floating_layout, groups, layouts
from components.keymaps import keys, mouse
from components.panel import screens, widget_defaults

main = None

prompt = f"{USER}@{HOSTNAME}: "

auto_fullscreen = True
bring_front_click = False
cursor_wrap = False

dgrous_key_binder = None
dgroups_app_rules = []

follow_mouse_focus = True
focus_on_window_activation = "focus"

wmname = "LG3D"
