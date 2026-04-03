import sys
import importlib.util
from pathlib import Path

from PyQt6.QtCore import QSize, Qt
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

from wyze_setbulbs import apply_scene


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Bedroom Lighting Switcher"
        self.setWindowTitle(self.title)

        # Initialize the tab widget and set it as central
        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)


class MyTabWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. Create the master layout for this entire widget
        main_layout = QVBoxLayout(self)

        # 2. Initialize the tab container and the individual tab pages
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        # 3. Add the pages to the tab container
        self.tabs.addTab(self.tab1, "Scene Switcher")
        self.tabs.addTab(self.tab2, "Scene Creator")

        # --- Setting up Tab 1 ---

        # Create a layout specifically for tab 1
        tab1_layout = QVBoxLayout()

        # Instantiate the widget (build the house from the blueprint)
        # We pass self.tab1 so the SceneSwitcher knows it lives inside tab1
        scene_switcher_widget = SceneSwitcher(self.tab1)

        # Add the instantiated widget to tab 1's layout
        tab1_layout.addWidget(scene_switcher_widget)

        # Finally, apply the layout to tab 1
        self.tab1.setLayout(tab1_layout)

        # --- Finishing up ---

        # Add the whole tab container to the master layout
        main_layout.addWidget(self.tabs)


class SceneSwitcher(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Pass 'self' so the grid layout knows it belongs to SceneSwitcher
        self.layout = QGridLayout(self)

        p = Path("/Users/alhar/wyze-lights-control/scenes")
        files = p.glob("*.py")

        rowCount = 0
        colCount = 0

        sys.path.append("scenes")

        for f in files:
            sceneName = f.name
            sceneName = sceneName.replace(".py", "").replace("-", " ").title()

            newButton = QPushButton(sceneName)

            # Create a spec for the module
            module_spec = importlib.util.spec_from_file_location(f.name, f)
            # Load the module from the spec
            f_module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(f_module)

            newButton.clicked.connect(
                lambda checked, config=f_module.bulbs_config: apply_scene(config)
            )

            self.layout.addWidget(newButton, rowCount, colCount)

            rowCount += 1
            if rowCount == 3:
                rowCount = 0
                colCount += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
