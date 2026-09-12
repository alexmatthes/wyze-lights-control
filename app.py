import sys
import json
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtGui import QIcon

# Order categories should appear in; anything else found in scene files is
# appended after these, alphabetically.
CATEGORY_ORDER = ["indoor", "outdoor"]
CATEGORY_LABELS = {"indoor": "Indoor", "outdoor": "Outdoor"}

from wyze_setbulbs import get_wyze_client, apply_scene


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller bundle."""
    if hasattr(sys, "_MEIPASS"):
        # Running as bundled exe — PyInstaller extracts to this temp dir
        base_path = Path(sys._MEIPASS)
    else:
        # Running as normal script
        base_path = Path(__file__).parent
    return base_path / relative_path


def external_path(relative_path):
    """Get absolute path to external resource, right next to the executable or script."""
    if getattr(sys, "frozen", False):
        # Running as bundled exe - get the folder containing the actual .exe
        base_path = Path(sys.executable).parent
    else:
        # Running as normal script
        base_path = Path(__file__).parent
    return base_path / relative_path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Bedroom Lighting Switcher"
        self.tab_widget = MyTabWidget(self)

        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(str(resource_path("icon.ico"))))
        self.setCentralWidget(self.tab_widget)


class MyTabWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        main_layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.tabs.addTab(self.tab1, "Scene Switcher")
        self.tabs.addTab(self.tab2, "Scene Creator")

        # Authenticate once at startup so button presses are near-instant
        self.client = get_wyze_client()

        # --- Tab 1: Scene Switcher ---
        tab1_layout = QVBoxLayout()
        scene_switcher_widget = SceneSwitcher(self.tab1, self.client)
        tab1_layout.addWidget(scene_switcher_widget)
        self.tab1.setLayout(tab1_layout)

        main_layout.addWidget(self.tabs)


class SceneSwitcher(QWidget):
    def __init__(self, parent=None, client=None):
        super().__init__(parent)
        self.client = client
        self.main_layout = QVBoxLayout(self)
        self._load_scenes()

    def _load_scenes(self):
        """Reads all .json files from the scenes folder and builds one button
        grid per category (indoor/outdoor/...), each under its own header."""

        # Use the new external_path function instead of resource_path
        scenes_path = external_path("scenes")

        # Prevent crashes if the scenes folder is missing
        if not scenes_path.exists():
            print(f"Scenes folder not found at {scenes_path}")
            return

        files = sorted(scenes_path.glob("*.json"))

        scenes_by_category = {}
        for f in files:
            with open(f, "r") as fh:
                scene = json.load(fh)
            category = scene.get("category", "indoor")
            scenes_by_category.setdefault(category, []).append(scene)

        ordered_categories = [c for c in CATEGORY_ORDER if c in scenes_by_category]
        ordered_categories += sorted(
            c for c in scenes_by_category if c not in CATEGORY_ORDER
        )

        MAX_COLS = 3

        for category in ordered_categories:
            header = QLabel(CATEGORY_LABELS.get(category, category.title()).upper())
            header.setObjectName("sectionHeader")
            self.main_layout.addWidget(header)

            section = QWidget()
            grid_layout = QGridLayout(section)
            row, col = 0, 0

            for scene in scenes_by_category[category]:
                button = QPushButton(scene["name"])
                button.setProperty("category", category)
                button.clicked.connect(
                    lambda checked, scene=scene: apply_scene(self.client, scene)
                )

                grid_layout.addWidget(button, row, col)
                col += 1
                if col == MAX_COLS:
                    col = 0
                    row += 1

            self.main_layout.addWidget(section)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open(resource_path("style.qss"), "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
