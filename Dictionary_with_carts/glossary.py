import json

import keyboard

from difflib import get_close_matches

from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox

from cart import Cart
from glossary_ui import Ui_MainWindow


class Glossary(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_file()
        self.add_first_items()
        self.list_widget_for_cart.itemSelectionChanged.connect(self.put_title_definition)
        self.edit_btn.clicked.connect(self.edit_btn_clicked)
        self.add_btn.clicked.connect(self.add_btn_clicked)
        self.delete_btn.clicked.connect(self.detele_choosen_word)
        if keyboard.is_pressed('Enter'):
            self.search_btn_clicked()
        self.search_btn.clicked.connect(self.search_btn_clicked)

    def upload_json(self):
        file = open('data_2.json', 'w')
        json.dump(self.data, file)

    def search_btn_clicked(self):
        self.list_widget_for_cart.clear()
        close_words = get_close_matches(self.search_paneli.text(), self.data)
        for word in close_words:
            # print(word)
            self.create_cart(word)

    def create_cart(self, word):
        cart = Cart()
        cart.title_lbl.setText(word)
        cart.define_lbl.setText(self.data[word][:100] if len(self.data[word]) < 100 else self.data[word][:100] + '...')
        item = QListWidgetItem()
        item.setSizeHint(cart.size())
        self.list_widget_for_cart.addItem(item)
        self.list_widget_for_cart.setItemWidget(item, cart)

    def detele_choosen_word(self):
        item = self.list_widget_for_cart.currentItem()
        widget = self.list_widget_for_cart.itemWidget(item)
        word: str = widget.title_lbl.text().lower()
        del self.data[word]
        # рабочий(удаляет)
        self.list_widget_for_cart.takeItem(self.list_widget_for_cart.currentRow())
        self.upload_json()

        # рабочий(удаляет)
        # self.list_widget_for_cart.takeItem(self.list_widget_for_cart.row())

        msb = QMessageBox()
        msb.information(self, 'Deleted', f'The word {word.title()} was successfully deleted')

        # self.list_widget_for_cart.removeItemWidget(item)

    # тоже работает(удаляет)
    # def detele_choosen_word(self):
    #     item = self.list_widget_for_cart.currentItem()
    #     try:
    #         if item:
    #             widget = self.list_widget_for_cart.itemWidget(item)
    #             word = widget.title_lbl.text().lower()
    #             del self.data[word]
    #             self.list_widget_for_cart.takeItem(self.list_widget_for_cart.row(item))
    #             # self.list_widget_for_cart.removeItemWidget(item)
    #     except Exception as error:
    #         QMessageBox.warning(self, "No Word Selected", error)

    # добавление новых слов в глоссарий(Title, definition)
    def add_btn_clicked(self):
        if self.change_word_structure.text() and self.set_definition.toPlainText():
            if self.change_word_structure.text().lower() not in self.data:
                text = self.set_definition.toPlainText().strip()
                self.data[self.change_word_structure.text().lower().strip()] = text
                cart = Cart()
                cart.title_lbl.setText(self.change_word_structure.text())
                # print(self.data)
                cart.define_lbl.setText(text[:100] if len(text) < 100 else text[:100] + '...')
                item = QListWidgetItem()
                item.setSizeHint(cart.size())
                self.list_widget_for_cart.addItem(item)
                self.list_widget_for_cart.setItemWidget(item, cart)
                self.upload_json()
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle('Alert')
                msgBox.setText("This word is already exists")
                msgBox.exec()

                # msgBox = QMessageBox()
                # msgBox.setWindowTitle('')
                # msgBox.setText("The document has been modified.")
                # msgBox.setInformativeText("Do you want to save your changes?")
                # msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
                # msgBox.setDefaultButton(QMessageBox.Save)
                # ret = msgBox.exec()

    # введение изменения на выделенную слову
    def edit_btn_clicked(self):
        item = self.list_widget_for_cart.currentItem()
        widget = self.list_widget_for_cart.itemWidget(item)
        if self.change_word_structure.text() and self.set_definition.toPlainText():
            widget.title_lbl.setText(self.change_word_structure.text().strip())
            widget.define_lbl.setText(self.set_definition.toPlainText()[:100].strip() if len(
                self.set_definition.toPlainText()) < 100 else self.set_definition.toPlainText()[:100] + '...')
            self.list_widget_for_cart.setItemWidget(item, widget)
            self.upload_json()

    # вставка названия и определения в редактор
    def put_title_definition(self):
        item = self.list_widget_for_cart.currentItem()
        if item:
            widget = self.list_widget_for_cart.itemWidget(item)
            self.change_word_structure.setText(widget.title_lbl.text())
            try:
                # вставка слова с json файла
                self.set_definition.setText(self.data[widget.title_lbl.text().lower()])
            except KeyError:
                # вставка слова с карты(если в json файле этого слова нет)
                # self.set_definition.setText(widget.define_lbl.text())
                print('dda')
                pass

    # с json файла в dict
    def load_file(self):
        file = open("data_2.json", 'r')
        self.data = json.load(file)
        # print(self.data)

    # добавение первый n-ых слов, продолжение
    def adding_first_items(self, title, define):
        item = QListWidgetItem()

        # widgetni yasash
        widget = Cart()
        widget.title_lbl.setText(title.title())
        widget.define_lbl.setText(define[:100] if len(define) < 100 else define[:100] + '...')

        # item qo'shish
        self.list_widget_for_cart.addItem(item)
        item.setSizeHint(widget.size())

        # itemga widgetni o'rmnatish
        self.list_widget_for_cart.setItemWidget(item, widget)

    # добавение первый n-ых слов
    def add_first_items(self):
        i = 0
        for key, value in self.data.items():
            if i == 200:
                break
            else:
                i += 1
                self.adding_first_items(key, value)

