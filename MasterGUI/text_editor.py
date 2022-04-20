import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QMainWindow):

    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        # Main UI code goes here
        # End Main UI code
        self.show()

        self.textedit = qtw.QTextEdit()
        self.setCentralWidget(self.textedit)

        self.statusBar().showMessage('Welcome to text_editor.py')   # 状态栏


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)    # 传递系统参数
    mw = MainWindow()
    sys.exit(app.exec())    # 可以在崩溃时传递部分给操作系统



