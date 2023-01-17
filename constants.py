import os
import socket

USER = os.environ["USER"]
HOSTNAME = socket.gethostname()
HOME = os.path.expanduser("~")
TERMINAL = "alacritty"
