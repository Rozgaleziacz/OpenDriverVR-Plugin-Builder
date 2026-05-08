# OpenDriver Plugin Builder

A simple GUI tool that streamlines building and installing plugins for OpenDriver on Windows.  
This project turns the classic CMake + Visual Studio workflow into a single click experience.

## Demo

https://github.com/user-attachments/assets/ce7351a4-4f65-49d5-a4f7-709b75cdd370

## Features

- One-click plugin build system  
- Automatic installation into OpenDriver plugins folder  
- Correct plugin structure generation  
- Automatic plugin.json handling  
- Live build output terminal  
- Clean build option  
- Auto detection of OpenDriver directory  
- Windows-friendly workflow  

## Download (Recommended)

Prebuilt version available (no Python required):

Latest release:
https://github.com/Rozgaleziacz/OpenDriverVR-Plugin-Builder/releases/latest

Go to Releases → Latest → Download ODVR Builder.exe

## Open Source Project

This project is fully open source.

- Original version is written in Python  
- Source code is available in this repository  
- Everything is transparent and editable  

You are free to fork it, modify it, improve it, and reuse it in your own tools.

No hidden logic, no closed components — everything is visible in the source code.

## OpenDriver Compatibility

Designed for OpenDriver VR:

https://github.com/Rozgaleziacz/OpenDriver-VR

Automatically installs plugins into:
%APPDATA%/opendriver/plugins

## Example Plugin Structure

plugins/
└── mouse_locomotion/
    ├── mouse_locomotion.dll
    └── plugin.json

## Requirements (for building from source)

- Python 3.9+
- CMake
- Visual Studio 2022 Build Tools
- Windows 10/11

Install dependencies:
pip install customtkinter

Run from source:
python main.py

## Build System

Internally runs:
cmake -B build
cmake --build build --config Release

Then automatically installs the compiled plugin into OpenDriver.

## Planned Features

- Hot reload system (instant plugin updates)  
- Plugin templates (Discord RPC, locomotion, trackers)  
- Dependency manager (ViGEm, Discord RPC, etc.)  
- Auto rebuild on file save  
- OpenDriver launcher integration  

## License

MIT License — fully open source project.
