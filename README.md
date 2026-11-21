# Sand Browser

A lightweight desktop web browser built with Python and **PyQt5** (`QtWebEngineWidgets`), featuring back/forward navigation, an address bar with `Enter` and **Go** button support, and automatic URL syncing.

## Features

- **Web Rendering:** Powered by `QWebEngineView` (defaulting to DuckDuckGo on startup).
- **Navigation Controls:** Back (`<`), Forward (`>`), single-line URL bar (`QLineEdit`), and a **Go** button.
- **Keyboard & URL Sync:** Press `Enter` to navigate, auto-prepends `https://` when a scheme is omitted, and updates the address bar as you browse.

## Installation (Arch Linux)

1. Install Python, core PyQt5, and build tools from the official repositories:

   ```bash
   sudo pacman -Syu python python-pyqt5 base-devel git
