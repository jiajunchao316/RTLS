# -*- coding: cp936 -*-
from PyQt4 import QtCore, QtGui
from ui_settingTab import Ui_setTab
import sys

class setTab(QtGui.QWidget):
    '''生成设置界面'''
    def __init__(self):
        super(setTab,self).__init__()
        self.ui = Ui_setTab()
        self.ui.setupUi(self)

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    settingTab = setTab()
    settingTab.show()
    sys.exit(app.exec_())
