import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QFileSystemModel,QTreeView, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form_widget = App()
        self.setCentralWidget(self.form_widget)

        self.setWindowTitle('Total Commander in python')
        self.setGeometry(1, 1, 1600, 1200)
        self.setWindowIcon(QIcon('tc.png'))

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Files')
        editMenu = mainMenu.addMenu('Mark')
        viewMenu = mainMenu.addMenu('Commands')
        searchMenu = mainMenu.addMenu('Net')
        toolsMenu = mainMenu.addMenu('Show')
        helpMenu = mainMenu.addMenu('Configuration')
        helpMenu = mainMenu.addMenu('Start')
        helpMenu = mainMenu.addMenu('Help')

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.model = QFileSystemModel()
        self.model.setRootPath('')

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.tree.resize(640, 480)

        self.tree2 = QTreeView()
        self.tree2.setModel(self.model)
        self.tree2.setAnimated(False)
        self.tree2.setIndentation(20)
        self.tree2.setSortingEnabled(True)
        self.tree2.resize(640, 480)

        vmain = QVBoxLayout()

        windowLayout = QHBoxLayout()
        windowLayout.addWidget(self.tree)
        windowLayout.addWidget(self.tree2)
        vmain.addLayout(windowLayout)

        vlayout = QHBoxLayout()
        a1 = QLabel('c:/> ')
        textbox = QLineEdit(self)
        vlayout.addWidget(a1)
        vlayout.addWidget(textbox)
        vmain.addLayout(vlayout)

        butbar = QHBoxLayout()
        b1 = QPushButton('F3 View')
        b2 = QPushButton('F4 Edit')
        b3 = QPushButton('F5 Copy')
        b4 = QPushButton('F6 Move')
        b5 = QPushButton('F7 New Folder')
        b6 = QPushButton('F8 Delete')
        b7 = QPushButton('Alt+F4 Exit')
        butbar.addWidget(b1)
        butbar.addWidget(b2)
        butbar.addWidget(b3)
        butbar.addWidget(b4)
        butbar.addWidget(b5)
        butbar.addWidget(b6)
        butbar.addWidget(b7)

        vmain.addLayout(butbar)

        self.setLayout(vmain)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    ex.show()
    sys.exit(app.exec_())
