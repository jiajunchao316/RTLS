# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnchCorrection.ui'
#
# Created: Tue Dec 01 12:00:32 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AnchTab(object):
    def setupUi(self, AnchTab):
        AnchTab.setObjectName(_fromUtf8("AnchTab"))
        AnchTab.resize(333, 300)
        self.gridLayout = QtGui.QGridLayout(AnchTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(AnchTab)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.savebpPB = QtGui.QPushButton(AnchTab)
        self.savebpPB.setObjectName(_fromUtf8("savebpPB"))
        self.gridLayout.addWidget(self.savebpPB, 1, 0, 1, 1)

        self.retranslateUi(AnchTab)
        QtCore.QMetaObject.connectSlotsByName(AnchTab)

    def retranslateUi(self, AnchTab):
        AnchTab.setWindowTitle(_translate("AnchTab", "Form", None))
        self.savebpPB.setText(_translate("AnchTab", "保存节点坐标", None))

