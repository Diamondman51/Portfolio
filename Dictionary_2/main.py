from PySide6.QtWidgets import QApplication

from glossary import Glossary

app = QApplication()

widget = Glossary()
widget.show()

app.exec()