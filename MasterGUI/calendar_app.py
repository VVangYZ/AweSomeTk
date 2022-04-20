import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class CategoryWindow(qtw.QWidget):

    submitted = qtc.pyqtSignal(str)

    def __init__(self):
        super(CategoryWindow, self).__init__(None, model=True)
        self.setLayout(qtw.QVBoxLayout())
        self.layout().addWidget(
            qtw.QLabel('Please enter a new category name:')
        )
        self.category_entry = qtw.QLineEdit()
        self.layout().addWidget(self.category_entry)
        self.submit_btn = qtw.QPushButton(
            'Submit',
            clicked=self.onSubmit
        )
        self.layout().addWidget(self.submit_btn)
        self.cancel_btn = qtw.QPushButton(
            'Cancel',
            clicked=self.close
        )
        self.layout().addWidget(self.cancel_btn)
        self.show()

    @qtc.pyqtSlot()
    def onSubmit(self):
        if self.category_entry.text():
            self.submitted.emit(self.category_entry.text())
        self.close()


class MainWindow(qtw.QWidget):
    events = {
        # QDate: {
        #     'title': "String title of event",
        #     'category': "String category of event",
        #     'time': QTime() or None if "all day",
        #     'detail': 'String details of event'
        # }
    }

    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        # Main UI code goes here

        self.setWindowTitle('My Calendar App')
        self.resize(800, 600)

        # Create widgets
        self.calendar = qtw.QCalendarWidget()
        self.event_list = qtw.QListWidget()
        self.event_title = qtw.QLineEdit()
        self.event_category = qtw.QComboBox()
        self.event_time = qtw.QTimeEdit(qtc.QTime(8, 0))
        self.allday_check = qtw.QCheckBox('All Day')
        self.event_detail = qtw.QTextEdit()
        self.add_button = qtw.QPushButton('Add/Update')
        self.del_button = qtw.QPushButton('Delete')

        # Configure some widgets
        self.event_category.addItems([
            'Select category...', 'New...', 'Work',
            'Meeting', 'Doctor', 'Family'
        ])
        self.event_category.model().item(0).setEnabled(False)   # 通过禁用组合框的第一个值来设定一个占位符

        # Arrange widgets
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

        # ------------------------------------------------------------------------------------------------------------
        # connect events

        self.allday_check.toggled.connect(self.event_time.setDisabled)      # 勾选 all day 则冻结时间选项
        self.calendar.selectionChanged.connect(self.populate_list)          # 日历改变日期，则 list 重新填写
        self.event_list.itemSelectionChanged.connect(                       # 事件列表变更，则填写表格？
            self.populate_form
        )
        self.add_button.clicked.connect(self.save_event)
        self.del_button.clicked.connect(self.delete_event)
        self.event_list.itemSelectionChanged.connect(       # signal 可以连接多个 slot
            self.check_delete_btn
        )
        self.check_delete_btn()     # 一开始变禁用

        # End Main UI code
        self.show()

    def clear_form(self):
        self.event_title.clear()
        self.event_category.setCurrentIndex(0)
        self.event_time.setTime(qtc.QTime(8, 0))
        self.allday_check.setChecked(False)
        self.event_detail.setPlainText('')

    def populate_list(self):
        self.event_list.setCurrentRow(-1)

        self.event_list.clear()
        self.clear_form()
        date = self.calendar.selectedDate()
        for event in self.events.get(date, []):
            time = (
                event['time'].toString('hh:mm')
                if event['time']
                else 'All Day'
            )
            self.event_list.addItem(f"{time}: {event['title']}")

    def populate_form(self):
        self.clear_form()
        date = self.calendar.selectedDate()
        event_number = self.event_list.currentRow()
        if event_number == -1:
            return
        event_data = self.events.get(date)[event_number]            # 获取当前 event
        self.event_category.setCurrentText(event_data['category'])  # event 选项更改
        if event_data['time'] is None:                              # 事件时间更改
            self.allday_check.setChecked(True)
        else:
            self.event_time.setTime(event_data['time'])
        self.event_title.setText(event_data['title'])               # 事件名称更改
        self.event_detail.setPlainText(event_data['detail'])        # 事件细节更改

    def save_event(self):
        event = {
            'category': self.event_category.currentText(),
            'time': (
                None
                if self.allday_check.isChecked()
                else self.event_time.time()
            ),
            'title': self.event_title.text(),
            'detail': self.event_detail.toPlainText()
        }
        date = self.calendar.selectedDate()
        event_list = self.events.get(date, [])
        event_number = self.event_list.currentRow()
        if event_number == -1:
            event_list.append(event)
        else:
            event_list[event_number] = event

        event_list.sort(key=lambda x: x['time'] or qtc.QTime(0, 0))
        self.events[date] = event_list
        self.populate_list()

    def delete_event(self):
        date = self.calendar.selectedDate()
        row = self.event_list.currentRow()
        del(self.events[date][row])
        self.event_list.setCurrentRow(-1)       # 切换未选择，则 delete 按钮
        self.clear_form()
        self.populate_list()

    def check_delete_btn(self):
        self.del_button.setDisabled(
            self.event_list.currentRow() == -1
        )

    def add_category(self, category):
        self.event_category.addItems(category)
        self.event_category.setCurrentText(category)

    def on_category_change(self, text):
        if text == 'New...':
            dialog = CategoryWindow()
            dialog.submitted.connect(self.add_category)
            self.event_category.setCurrentIndex(0)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)    # 传递系统参数
    mw = MainWindow()
    sys.exit(app.exec())    # 可以在崩溃时传递部分给操作系统



