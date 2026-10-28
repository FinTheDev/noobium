# Noobium

A customizable desktop browser built with Python and Qt WebEngine.
All because Google Chrome didn't allow theme customization without developer mode.

PAYBACK LOL

## Features

- Chromium-based web rendering
- Custom browser interface
- Tab management
- Customizable themes
- Bookmarks and browsing history
- Download management

## Tech stack

- Python
- PySide6
- Qt WebEngine

## Development

### Requirements

- Linux
- Python 3
- Qt 6 WebEngine
- PySide6

### Setup

```bash
git clone https://github.com/FinTheDev/noobium.git
cd noobium

python -m venv .venv
source .venv/bin/activate

sudo pacman -S python-pyside6 qt6-webengine

python -m noobium.browser
```

## Status

Early development. Features and APIs may change.

## License

See LICENSE.
