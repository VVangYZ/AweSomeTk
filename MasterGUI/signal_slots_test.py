import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QWidget):

    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        # Main UI code goes here
        self.entry1 = qtw.QLineEdit()
        self.entry2 = qtw.QLineEdit()
        self.good_button = qtw.QPushButton('Good')

        layout = qtw.QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.entry1)
        layout.addWidget(self.entry2)
        layout.addWidget(self.good_button)

        # self.entry1.textChanged.connect(self.entry2.setText)
        self.entry2.textChanged.connect(print)

        self.entry1.editingFinished.connect(lambda: print('editing finished'))
        self.entry2.returnPressed.connect(self.entry1.editingFinished)

        self.good_button.clicked.connect(self.no_args)

        # End Main UI code
        self.show()

    def no_args(self):
        print('I need no arguments')


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)    # 传递系统参数
    mw = MainWindow()
    sys.exit(app.exec())    # 可以在崩溃时传递部分给操作系统



