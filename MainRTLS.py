# -*- coding: cp936 -*-
from PyQt4 import QtCore, QtGui
from ui_MainRTLS import Ui_MainWindow
from draw.draw import GraphWidget,MS
from tabs.AnchCorrection import AnchTab
from tabs.settingTab import setTab
from uart.uart import SerachCK,MySerial,ReadCK
import sys
import math
from threading import Thread
import serial.tools.list_ports


class MianWindow(QtGui.QMainWindow):
    '''软件界面框架'''
    def __init__(self):
        super(MianWindow,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ms = MS()
        self.GW = GraphWidget(self.ms)
        self.AnchCor = AnchTab(self.GW)
        self.setTab = setTab()

        self.ui.gridLayout.addWidget(self.GW)
        self.createActions()
        self.createMenus()

        self.SCK = SerachCK(self.ui)
        self.SCK.setDaemon(True)
        self.SCK.start()

        self.myser = MySerial(self.ui,self.AnchCor,self.ms)
        self.ui.CKcomboBox.activated[str].connect(self.myser.selectCK)
        self.ui.openPB.clicked.connect(self.myser.openCK)
        self.ui.closePB.clicked.connect(self.myser.closeCK)

    def createActions(self):
        self.setAct = QtGui.QAction(u"&设置", self, shortcut="Ctrl+s",
                statusTip=u"基本设置",triggered=self.setting)

        self.addAnchAct = QtGui.QAction(u"&添加节点", self, shortcut="Ctrl+a",
                statusTip=u"添加节点",triggered=self.addAnch)

        self.exitAct = QtGui.QAction(u"&退出", self, shortcut="Ctrl+q",
                statusTip=u"退出程序",triggered=QtGui.qApp.closeAllWindows)

        self.aboutAct = QtGui.QAction(u"&帮助", self, shortcut="Ctrl+h",
                statusTip=u"使用向导",triggered=self.helpText)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu(u"&选项")
        self.fileMenu.addAction(self.setAct)
        self.fileMenu.addAction(self.addAnchAct)
        self.fileMenu.addAction(self.exitAct)
        self.helpMenu = self.menuBar().addMenu(u"&帮助")
        self.helpMenu.addAction(self.aboutAct)

    def setDockWindowAnch(self):
        dockAnch = QtGui.QDockWidget(u"参考节点坐标", self)
        dockAnch.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        dockAnch.setWidget(self.AnchCor)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dockAnch)

    def setDockWindowSet(self):
        dockSet = QtGui.QDockWidget(u"设置", self)
        dockSet.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        dockSet.setWidget(self.setTab)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dockSet)

    def setting(self):
        self.setDockWindowSet()

    def addAnch(self):
        self.setDockWindowAnch()

    def helpText(self):
        pass

    

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    MianW = MianWindow()
    MianW.show()
    sys.exit(app.exec_())

