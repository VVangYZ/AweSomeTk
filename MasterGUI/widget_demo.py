import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QWidget):

    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        # Main UI code goes here

        subwidget = qtw.QWidget(self)
        subwidget.setToolTip('This is good')

        # create basic widgets
        label = qtw.QLabel('Hello Widgets!', self)
        line_edit = qtw.QLineEdit('default value', self)
        button = qtw.QPushButton("Push Me", self)
        combobox = qtw.QComboBox(self)
        combobox.addItem('Lemon', 1)
        combobox.addItem('Peach', 'Ohh I like Peaches!')
        combobox.addItem('Strawberry', qtw.QWidget)
        combobox.insertItem(1, 'Radish', 2)

        textedit = qtw.QTextEdit(self)
        textedit.setAcceptRichText(False)
        textedit.setLineWrapColumnOrWidth(25)
        textedit.setPlaceholderText('Enter your text here')

        # create layout
        layout = qtw.QVBoxLayout()      # 创建布局并赋予
        self.setLayout(layout)
        layout.addWidget(label)
        # layout.addWidget(line_edit)

        sublayout = qtw.QHBoxLayout()       # 水平、垂直布局
        layout.addLayout(sublayout)
        sublayout.addWidget(button)
        sublayout.addWidget(combobox)

        grid_layout = qtw.QGridLayout()     # 网格布局
        # layout.addLayout(grid_layout)
        grid_layout.addWidget(line_edit, 0, 0)
        # grid_layout.addWidget(label, 0, 1)
        grid_layout.addWidget(textedit, 1, 0, 2, 2)

        form_layout = qtw.QFormLayout()     # 双列模式
        layout.addLayout(form_layout)
        form_layout.addRow('Item 1', qtw.QLineEdit(self))
        form_layout.addRow('Item 2', qtw.QLineEdit(self))
        form_layout.addRow(qtw.QLabel('<b>This is a label-only row</b>'))

        # container widget
        tab_widget = qtw.QTabWidget()
        layout.addWidget(tab_widget)
        container = qtw.QWidget(self)
        container.setLayout(grid_layout)
        tab_widget.addTab(container, 'Tab the first')
        tab_widget.addTab(subwidget, 'Tab the second')

        groupbox = qtw.QGroupBox('Button')
        groupbox.setLayout(qtw.QHBoxLayout())
        groupbox.layout().addWidget(qtw.QPushButton('OK'))
        groupbox.layout().addWidget(qtw.QPushButton('Cancel'))
        layout.addWidget(groupbox)

        # End Main UI code
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)    # 传递系统参数
    mw = MainWindow()
    sys.exit(app.exec())    # 可以在崩溃时传递部分给操作系统


