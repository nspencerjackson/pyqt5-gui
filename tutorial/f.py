import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("brws.ui",self)
        self.browse.clicked.connect(self.browsefiles)

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(self,"Open File", "C:\\Users\\nspen\\Documents")
        self.directory.setText(fname[0])

app = QApplication(sys.argv)
mw = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.setFixedWidth(400)
widget.setFixedHeight(300)
widget.show()
sys.exit(app.exec_())
