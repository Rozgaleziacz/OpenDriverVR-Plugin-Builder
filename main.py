import customtkinter as ctk
from tkinter import filedialog
import subprocess
import threading
import os
import shutil
from pathlib import Path

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ODVRBuilderApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("OpenDriver Plugin Builder")
        self.geometry("1000x650")

        # =========================
        # Paths
        # =========================

        self.plugin_path = ctk.StringVar()
        self.build_path = ctk.StringVar()

        self.odvr_plugins_path = os.path.join(
            os.environ["APPDATA"],
            "opendriver",
            "plugins"
        )

        # =========================
        # UI
        # =========================

        title = ctk.CTkLabel(
            self,
            text="OpenDriver Plugin Builder",
            font=("Segoe UI", 28, "bold")
        )
        title.pack(pady=20)

        # -------------------------
        # Plugin folder
        # -------------------------

        plugin_frame = ctk.CTkFrame(self)
        plugin_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            plugin_frame,
            text="Plugin Folder:"
        ).pack(anchor="w", padx=10, pady=(10, 0))

        plugin_row = ctk.CTkFrame(plugin_frame, fg_color="transparent")
        plugin_row.pack(fill="x", padx=10, pady=10)

        self.plugin_entry = ctk.CTkEntry(
            plugin_row,
            textvariable=self.plugin_path
        )
        self.plugin_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        browse_plugin_btn = ctk.CTkButton(
            plugin_row,
            text="Browse",
            command=self.select_plugin_folder
        )
        browse_plugin_btn.pack(side="right")

        # -------------------------
        # Build folder
        # -------------------------

        build_frame = ctk.CTkFrame(self)
        build_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            build_frame,
            text="Build Folder:"
        ).pack(anchor="w", padx=10, pady=(10, 0))

        build_row = ctk.CTkFrame(build_frame, fg_color="transparent")
        build_row.pack(fill="x", padx=10, pady=10)

        self.build_entry = ctk.CTkEntry(
            build_row,
            textvariable=self.build_path
        )
        self.build_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        browse_build_btn = ctk.CTkButton(
            build_row,
            text="Browse",
            command=self.select_build_folder
        )
        browse_build_btn.pack(side="right")

        # -------------------------
        # OpenDriver folder
        # -------------------------

        odvr_frame = ctk.CTkFrame(self)
        odvr_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            odvr_frame,
            text=f"OpenDriver Plugins Folder:\n{self.odvr_plugins_path}"
        ).pack(anchor="w", padx=10, pady=10)

        # -------------------------
        # Buttons
        # -------------------------

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(fill="x", padx=20, pady=10)

        build_btn = ctk.CTkButton(
            button_frame,
            text="BUILD",
            height=40,
            command=self.start_build
        )
        build_btn.pack(side="left", padx=10, pady=10)

        build_install_btn = ctk.CTkButton(
            button_frame,
            text="BUILD + INSTALL",
            height=40,
            command=self.start_build_install
        )
        build_install_btn.pack(side="left", padx=10, pady=10)

        clean_btn = ctk.CTkButton(
            button_frame,
            text="CLEAN BUILD",
            height=40,
            command=self.clean_build
        )
        clean_btn.pack(side="left", padx=10, pady=10)

        # -------------------------
        # Terminal
        # -------------------------

        terminal_frame = ctk.CTkFrame(self)
        terminal_frame.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            terminal_frame,
            text="Build Output",
            font=("Segoe UI", 18, "bold")
        ).pack(anchor="w", padx=10, pady=10)

        self.terminal = ctk.CTkTextbox(
            terminal_frame,
            font=("Consolas", 13)
        )
        self.terminal.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.log("OpenDriver Builder Ready 🚀")

    # ======================================
    # Logging
    # ======================================

    def log(self, text):
        self.terminal.insert("end", text + "\n")
        self.terminal.see("end")

    # ======================================
    # Folder Selectors
    # ======================================

    def select_plugin_folder(self):
        folder = filedialog.askdirectory()

        if folder:
            self.plugin_path.set(folder)

            auto_build = os.path.join(folder, "build")
            self.build_path.set(auto_build)

    def select_build_folder(self):
        folder = filedialog.askdirectory()

        if folder:
            self.build_path.set(folder)

    # ======================================
    # Build Logic
    # ======================================

    def start_build(self):
        threading.Thread(
            target=self.build_plugin,
            daemon=True
        ).start()

    def start_build_install(self):
        threading.Thread(
            target=self.build_and_install,
            daemon=True
        ).start()

    def run_command(self, command, cwd=None):

        self.log(f"> {' '.join(command)}")

        process = subprocess.Popen(
            command,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            shell=True
        )

        for line in process.stdout:
            self.log(line.rstrip())

        process.wait()

        return process.returncode

    def build_plugin(self):

        plugin_dir = self.plugin_path.get()
        build_dir = self.build_path.get()

        if not plugin_dir:
            self.log("❌ No plugin folder selected")
            return

        Path(build_dir).mkdir(parents=True, exist_ok=True)

        self.log("================================")
        self.log("Starting Build...")
        self.log("================================")

        # Configure
        result = self.run_command(
            ["cmake", "-B", build_dir],
            cwd=plugin_dir
        )

        if result != 0:
            self.log("❌ CMake configure failed")
            return

        # Build
        result = self.run_command(
            ["cmake", "--build", build_dir, "--config", "Release"],
            cwd=plugin_dir
        )

        if result != 0:
            self.log("❌ Build failed")
            return

        self.log("✅ Build completed successfully")

    # ======================================
    # Install
    # ======================================

    def build_and_install(self):

        self.build_plugin()

        build_dir = self.build_path.get()
        plugin_dir = self.plugin_path.get()

        release_dir = os.path.join(build_dir, "Release")

        if not os.path.exists(release_dir):
            self.log("❌ Release folder not found")
            return

        dlls = list(Path(release_dir).glob("*.dll"))

        if not dlls:
            self.log("❌ No DLL found")
            return

        plugin_json = os.path.join(plugin_dir, "plugin.json")

        if not os.path.exists(plugin_json):
            self.log("❌ plugin.json not found")
            return

        os.makedirs(self.odvr_plugins_path, exist_ok=True)

        for dll in dlls:

            plugin_name = dll.stem

            target_folder = os.path.join(
                self.odvr_plugins_path,
                plugin_name
            )

            os.makedirs(target_folder, exist_ok=True)

            # DLL
            target_dll = os.path.join(
                target_folder,
                dll.name
            )

            shutil.copy2(dll, target_dll)

            # plugin.json
            target_json = os.path.join(
                target_folder,
                "plugin.json"
            )

            shutil.copy2(plugin_json, target_json)

            self.log(f"📦 Installed plugin: {plugin_name}")

    

    # ======================================
    # Clean
    # ======================================

    def clean_build(self):

        build_dir = self.build_path.get()

        if not build_dir:
            self.log("❌ No build folder selected")
            return

        if os.path.exists(build_dir):

            shutil.rmtree(build_dir)

            self.log("🧹 Build folder deleted")

        else:
            self.log("⚠ Build folder does not exist")


app = ODVRBuilderApp()
app.mainloop()