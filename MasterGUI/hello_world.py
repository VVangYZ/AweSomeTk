from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])    # 需在任何 Qt widgets 之前创造
window = QtWidgets.QWidget()
window.setWindowTitle('Hello, World!')
window.show()
app.exec()





