# OpenDriver Plugin Builder

Simple GUI tool for building and installing OpenDriver plugins on Windows.

## Features

- One-click plugin building
- Auto install to OpenDriver
- Live terminal output
- Auto copy `plugin.json`
- Auto create plugin folders
- Clean build button

## Requirements

- CMake
- Visual Studio 2022 Build Tools
- OpenDriver

## Usage

Launch:

```text
ODVR Builder.exe
Select your plugin folder
Click BUILD + INSTALL
Plugin is automatically installed into OpenDriver
OpenDriver Plugin Path

The app automatically detects:

%APPDATA%/opendriver/plugins
Example Plugin Structure
plugins/
└── my_plugin/
    ├── my_plugin.dll
    └── plugin.json
Planned Features
Hot Reload
Plugin templates
Auto dependency copy
Auto rebuild on save
OpenDriver launcher
License

MIT