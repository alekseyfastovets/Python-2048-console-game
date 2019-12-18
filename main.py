
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import random
import game2048
from game2048 import game2048
from ui_2048 import Ui_MainWindow
import sys


class GUI_2048(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.logic = game2048()
        self.ui.setupUi(self)
        self.field = int(self.ui.comboBox.text())
        self.ui.tableWidget.setColumnCount(self.field)
        self.ui.tableWidget.setRowCount(self.field)
        self.ui.comboBox.addItem("3")
        self.ui.comboBox.addItem("4")
        self.ui.comboBox.addItem("5")
        self.ui.comboBox_2.addItem("2")
        self.ui.comboBox_2.addItem("3")
        self.ui.comboBox_2.addItem("4")
        self.ui.pushButton.clicked.connect(self.start)

    def start(self):
        for key, value in enumerate(self.logic.field):
            for i, elem in enumerate(value):
                item = QTableWidgetItem(str(elem))
                self.ui.tableWidget.setItem(key,i,item)
    #def step(self):
        
        
        
        
app = QtWidgets.QApplication(sys.argv)
application = GUI_2048()
application.show()

sys.exit(app.exec())
