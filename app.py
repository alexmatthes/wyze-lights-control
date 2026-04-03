import sys
import importlib.util

from PyQt6.QtCore import QSize, Qt,pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QWidget
from pathlib import Path
from wyze_setbulbs import apply_scene

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Scene Switcher")

    layout = QGridLayout()

    p = Path('/Users/alhar/wyze-lights-control/scenes')
    files = p.glob('*.py')

    rowCount = 0
    colCount = 0

    for f in files:
      sceneName = f.name
      sceneName = sceneName.replace(".py", "")
      sceneName = sceneName.replace("-", " ")
      sceneName = sceneName.title()

      newButton = QPushButton(sceneName)

      # Create a spec for the module
      module_spec = importlib.util.spec_from_file_location(f.name, f)

      # Load the module from the spec
      f_module = importlib.util.module_from_spec(module_spec)

      sys.path.append('scenes')

      module_spec.loader.exec_module(f_module)

      newButton.clicked.connect(lambda checked, config=f_module.bulbs_config: apply_scene(config))

      layout.addWidget(newButton, rowCount, colCount)

      rowCount += 1

      if (rowCount == 3):
        rowCount = 0
        colCount += 1

    widget = QWidget()
    widget.setLayout(layout)

    self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
