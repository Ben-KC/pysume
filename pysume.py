import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QTreeView, QHBoxLayout)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Pysume"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

        self.tree = QTreeView()
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.tree)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
