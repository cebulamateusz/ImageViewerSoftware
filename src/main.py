import sys
import os

from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication
import logging
import traceback
from Widgets.MainWindow.MainWindowWidget import MainWindowWidget

def global_exception_handler():
    error_message = 'Server exception:\n' + ''.join(traceback.format_exception(*sys.exc_info()))
    logging.error(error_message)

app = QApplication(sys.argv)
style = '''
        /* Dark Mode Style Sheet */

/* Set application-wide properties */
QWidget {
    background-color: #1e1e1e;
    color: #f0f0f0;
    font-size: 12px;
}

/* Button styles */
QPushButton {
    background-color: #353535;
    color: #f0f0f0;
    border: 1px solid #505050;
    border-radius: 4px;
    padding: 5px;
}

QPushButton:hover {
    background-color: #454545;
}

/* Toggle Button styles */
QPushButton:checked {
    background-color: #007acc;
    color: #f0f0f0;
}

/* Line Edit styles */
QLineEdit {
    background-color: #2e2e2e;
    color: #f0f0f0;
    border: 1px solid #505050;
    border-radius: 4px;
    padding: 5px;
}

/* Scroll Bar styles */
QScrollBar:vertical {
    border: none;
    background: #1e1e1e;
    width: 14px;
}

QScrollBar::handle:vertical {
    background: #3a3a3a;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background: #444444;
}

QScrollBar::add-line:vertical {
    background: none;
}

QScrollBar::sub-line:vertical {
    background: none;
}

        '''
app.setStyleSheet(style)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
sys.excepthook = global_exception_handler


window = MainWindowWidget()
window.show()
app.exec()
