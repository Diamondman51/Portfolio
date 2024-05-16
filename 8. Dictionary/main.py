from PySide6.QtWidgets import QApplication

from Widget import Widget
from PySide6.QtCore import QFile

# Import the compiled resource module
import Icons.icons

# Example of how to access an icon from the resource module
# icon_file = QFile("icon1.png")


app = QApplication()
widget = Widget()
widget.show()
app.exec()