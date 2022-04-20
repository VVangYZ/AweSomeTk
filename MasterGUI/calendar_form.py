import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QWidget):

    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        # Main UI code goes here

        self.setWindowTitle('My Calendar App')
        self.resize(800, 600)

        # widgets
        self.calendar = qtw.QCalendarWidget()
        self.event_list = qtw.QListWidget()
        self.event_title = qtw.QLineEdit()
        self.event_category = qtw.QComboBox()
        self.event_time = qtw.QTimeEdit(qtc.QTime(8, 0))
        self.allday_check = qtw.QCheckBox('All Day')
        self.event_detail = qtw.QTextEdit()
        self.add_button = qtw.QPushButton('Add/Update')
        self.del_button = qtw.QPushButton('Delete')

        self.event_category.addItems([
            'Select category...', 'New...', 'Work',
            'Meeting', 'Doctor', 'Family'
        ])
        self.event_category.model().item(0).setEnabled(False)   # 通过禁用组合框的第一个值来设定一个占位符

        # layout
        main_layout = qtw.QHBoxLayout()         # 整体组织
        self.setLayout(main_layout)
        main_layout.addWidget(self.calendar)    # 添加日历
        self.calendar.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding
        )

        right_layout = qtw.QVBoxLayout()        # 右侧组织
        main_layout.addLayout(right_layout)
        right_layout.addWidget(qtw.QLabel('Events on Date'))    # 添加文字
        right_layout.addWidget(self.event_list)                 # 添加事件列表
        self.event_list.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding
        )

        event_form = qtw.QGroupBox('Event')                     # 分组框
        right_layout.addWidget(event_form)                      # 添加分组框到布局
        event_form_layout = qtw.QGridLayout()                   # 分组框内设置网格布局
        event_form.setLayout(event_form_layout)

        event_form_layout.addWidget(self.event_title, 1, 1, 1, 3)       # 事件框
        event_form_layout.addWidget(self.event_category, 2, 1)          # 事件目录
        event_form_layout.addWidget(self.event_time, 2, 2)              # 事件时间
        event_form_layout.addWidget(self.allday_check, 2, 3)            # 全天勾选框
        event_form_layout.addWidget(self.event_detail, 3, 1, 1, 3)      # 事件详情
        event_form_layout.addWidget(self.add_button, 4, 2)              # 添加、编辑按钮
        event_form_layout.addWidget(self.del_button, 4, 3)              # 删除按钮

        # End Main UI code
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)    # 传递系统参数
    mw = MainWindow()
    sys.exit(app.exec())    # 可以在崩溃时传递部分给操作系统



