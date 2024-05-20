import json

from PySide6.QtCore import QSize, QItemSelection
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QWidget

from cart import Cart
from glossary_ui import Ui_MainWindow


class Glossary(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_file()
        i = 0
        for key, value in self.data.items():
            i += 1
            self.add_clicked(key, value)
            if i == 100:
                break

        self.list_widget_for_cart.currentItem()
        self.edit_btn.clicked.connect(self.add_clicked(self.change_word_structure.text(), self.set_definition.toPlainText()))


    def set_for_edit(self, title, define):
        self.change_word_structure.setText(title)
        self.set_definition.setText(define)

    def item_to_widget(self, item: QListWidgetItem):
        widget = self.list_widget_for_cart.itemWidget(item)
        self.change_word_structure.setText(widget.title_lbl.text())
        self.set_definition.setText(widget.define_lbl.text())


    def load_file(self):
        file = open("data.json", 'r')
        self.data = json.load(file)
        # print(self.data)

    def add_clicked(self, title, define):
        item = QListWidgetItem()

        # widgetni yasash
        widget = Cart()
        widget.title_lbl.setText(title.title())
        widget.define_lbl.setText(define[:1000])

        # item qo'shish
        self.list_widget_for_cart.addItem(item)
        item.setSizeHint(widget.size())

        # itemga widgetni o'rmnatish
        self.list_widget_for_cart.setItemWidget(item, widget)