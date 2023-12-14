import sys
import os
from PyQt5.QtWidgets import QApplication
import logging
import traceback
from Widgets.MainWindow.MainWindowWidget import MainWindowWidget

def global_exception_handler():
    error_message = 'Server exception:\n' + ''.join(traceback.format_exception(*sys.exc_info()))
    logging.error(error_message)

app = QApplication(sys.argv)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
sys.excepthook = global_exception_handler


window = MainWindowWidget()
window.show()
app.exec()
