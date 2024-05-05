from PySide6.QtWidgets import QApplication

from Window import Window

app = QApplication()
window = Window()
window.show()
app.exec()