import os
import sys
from pathlib import Path

# os.system("sudo apt-get install -y python3-dev libasound2-dev")
os.system("pip3 install -U pip wheel setuptools")
os.system("pip3 install -r requirements.txt")

desktop_file = '{}/.local/share/applications/warp-gui.desktop'.format(Path.home())

file = open(desktop_file, 'w+')
cur_path = sys.path[0]
file.write('''[Desktop Entry]
Name= Warp Cloudflare 
Comment= a gui app base on warp-cli for linux
Exec= python3 {}/main.py
Icon= {}/logo.png
Terminal=false
Type=Application
StartupNotify=true'''.format(cur_path, cur_path))

print('Desktop file created at "{}"'.format(desktop_file))
