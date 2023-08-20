# Warp Cloudflare GUI

A GUI application based on [warp-cli](https://developers.cloudflare.com/warp-client/get-started/linux) for Linux.

## Quick Access

- [Installation](#installation)
- [Hidden Mode](#hidden-mode)
- [Uninstall](#uninstall)
- [Screenshot](#screenshot)
- [Resolved Issues](#resolved-issues)

## Installation

Read the [warp-cli install](https://developers.cloudflare.com/warp-client/get-started/linux) documentation. Install `warp-cli` and
register with the `$ warp-cli register` command.

Then execute the following commands:

    $ git clone https://github.com/mrmoein/warp-cloudflare-gui
    $ cd warp-cloudflare-gui
    $ python3 install.py
    $ sudo chmod +x ~/.local/share/applications/warp-gui.desktop

Now search for `warp cloudflare` in your desktop menu.

> ⚠️ IMPORTANT: After the installation please make sure you do not remove the repository directory. It is required for the desktop shortcut to work.

## Hidden Mode
If you only want to use the tray icon, you can run the program in hidden mode.
    
    $ python ./main.py --hide

## Uninstall

Just remove the `~/.local/share/applications/warp-gui.desktop` file.

## Screenshot

![warp cloudflare gui](icons/Screenshot.png)

## Resolved Issues
- [There are 2 tray icons of WARP CLI and this GUI app](https://github.com/mrmoein/warp-cloudflare-gui/issues/11)
