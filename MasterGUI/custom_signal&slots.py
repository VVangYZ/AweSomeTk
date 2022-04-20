import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QWidget):

    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        # Main UI code goes here

        self.setLayout(qtw.QVBoxLayout())

        self.label = qtw.QLabel('Click "change" to change this text.')
        self.change = qtw.QPushButton("Change", clicked=self.onChange)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.change)

        # End Main UI code
        self.show()

    @qtc.pyqtSlot()          # 可以设置为 slot，也可以实现数据安全（指定类型参数）
    def onChange(self):
        self.formwindow = FormWindow()
        self.formwindow.submitted.connect(self.label.setText)
        self.formwindow.show()


class FormWindow(qtw.QWidget):
    submitted = qtc.pyqtSignal(str)     # 创建自己的 signal

    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())

        self.edit = qtw.QLineEdit()
        self.submit = qtw.QPushButton('Submit', clicked=self.onSubmit)
        self.layout().addWidget(self.edit)
        self.layout().addWidget(self.submit)

    def onSubmit(self):
        self.submitted.emit(self.edit.text())       # 发射信号
        self.close()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)    # 传递系统参数
    mw = MainWindow()
    sys.exit(app.exec())    # 可以在崩溃时传递部分给操作系统



