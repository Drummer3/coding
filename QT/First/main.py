# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dashboard')
        self.setStyleSheet("QMainWindow {background: 'black';}")
        self.showMaximized()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
