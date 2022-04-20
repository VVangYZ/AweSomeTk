# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#
#     w = QWidget()
#     w.resize(250, 150)
#     w.move(300, 300)
#     w.setWindowTitle('PYQT Test')
#     w.show()
#
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QPushButton, QWidget, QToolTip
from PyQt5.QtGui import QIcon, QFont


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        # super(MainWindow.self).__init__(parent)
        super().__init__(parent)

        # 预设
        self.resize(400, 200)
        self.status = self.statusBar()
        self.status.showMessage("这种状态栏提示", 5000)

        # 气泡提示
        self.setWindowTitle("PyQt MainWindow 例子")
        QToolTip.setFont(QFont('SamsSerif', 10))
        self.setToolTip('这是一个气泡提示')

        # 设置按钮
        self.button1 = QPushButton('关闭主窗口')
        self.button1.clicked.connect(self.onButtonClick)    # 关联函数

        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self):
        sender = self.sender()      # 获得发送信号的对象（此为“关闭主窗口”的按钮控件）
        print(sender.text() + '被按下了')
        qApp = QApplication.instance()      # 获取 QApplication 对象，调用关闭函数
        qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec())


