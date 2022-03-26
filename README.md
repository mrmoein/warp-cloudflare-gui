# warp cloudflare gui

a GUI app base on [warp-cli](https://developers.cloudflare.com/warp-client/get-started/linux) for linux

## Installation

Read [warp-cli install doc](https://developers.cloudflare.com/warp-client/get-started/linux). install `warp-cli` and
register with `$ warp-cli register`.

and then:

```
git clone https://github.com/mrmoein/warp-cloudflare-gui
cd warp-cloudflare-gui
python3 install.py
sudo chmod +x ~/.local/share/applications/warp-gui.desktop
```

now search for `warp cloudflare` app in your desktop menu.

> ⚠️ IMPORTANT: After the installation please make sure you do not remove the repository. It is required for the desktop shortcut to work.

## Uninstall

Just remove `~/.local/share/applications/warp-gui.desktop` file.

## Screenshot

![warp cloudflare gui](icons/Screenshot.png)