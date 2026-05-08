# OpenDriver Plugin Builder

A simple GUI tool that streamlines building and installing plugins for OpenDriver on Windows.

This project turns the messy CMake + Visual Studio workflow into a single click experience.

---

## 🎬 Demo

> Add a short video/gif here showing:
> - selecting a plugin folder
> - clicking BUILD + INSTALL
> - plugin appearing in OpenDriver

```text


https://github.com/user-attachments/assets/b21c370a-3781-4859-bc31-06dcf05acbb1


⚡ Features
One-click plugin build system
Automatic installation into OpenDriver plugins folder
Correct plugin structure generation
Copies plugin.json automatically
Live build output terminal
Clean build option
Auto detection of OpenDriver directory
Windows-ready workflow
📦 Download (Recommended)

You can download a precompiled version (no Python needed):

👉 Latest release:
https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/releases/latest

Go to Releases → Latest → Download ODVR Builder.exe

🧠 Open Source Project

This project is fully open source.

Original implementation is written in Python
Source code is available in this repository (top-level files)
You are free to:
modify it
fork it
improve it
use it in your own tools

No hidden binaries, no closed logic — everything is visible in the source code.

📁 OpenDriver Compatibility

This tool is designed specifically for:

👉 OpenDriver VR project
https://github.com/OpenDriver-VR/OpenDriver

It automatically installs plugins into:

%APPDATA%/opendriver/plugins
🧩 Example Plugin Structure
plugins/
└── mouse_locomotion/
    ├── mouse_locomotion.dll
    └── plugin.json
🛠 Requirements (for building from source)

If you want to run from source:

Python 3.9+
CMake
Visual Studio 2022 Build Tools
Windows 10/11

Install dependencies:

pip install customtkinter

Run:

python main.py
🚀 Build system

Internally the tool runs:

cmake -B build
cmake --build build --config Release

Then automatically installs the resulting plugin into OpenDriver.

🔧 Planned Features
Hot reload system (instant plugin reload)
Plugin templates (Discord RPC, locomotion, trackers)
Dependency manager (ViGEm, Discord RPC, etc.)
Auto rebuild on file save
OpenDriver launcher integration
📜 License

MIT License — fully open source, no restrictions.
