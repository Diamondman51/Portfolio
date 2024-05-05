from PySide6.QtWidgets import QApplication

from window import Window

app = QApplication()
wind = Window()
wind.show()
app.exec()