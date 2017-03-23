# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainRTLS.ui'
#
# Created: Mon Nov 30 13:56:38 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(890, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(581, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.CKcomboBox = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CKcomboBox.sizePolicy().hasHeightForWidth())
        self.CKcomboBox.setSizePolicy(sizePolicy)
        self.CKcomboBox.setMinimumSize(QtCore.QSize(70, 20))
        self.CKcomboBox.setMaximumSize(QtCore.QSize(150, 20))
        self.CKcomboBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.CKcomboBox.setObjectName(_fromUtf8("CKcomboBox"))
        self.gridLayout_3.addWidget(self.CKcomboBox, 0, 2, 1, 1)
        self.openPB = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openPB.sizePolicy().hasHeightForWidth())
        self.openPB.setSizePolicy(sizePolicy)
        self.openPB.setMaximumSize(QtCore.QSize(80, 20))
        self.openPB.setObjectName(_fromUtf8("openPB"))
        self.gridLayout_3.addWidget(self.openPB, 0, 3, 1, 1)
        self.closePB = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closePB.sizePolicy().hasHeightForWidth())
        self.closePB.setSizePolicy(sizePolicy)
        self.closePB.setMaximumSize(QtCore.QSize(80, 20))
        self.closePB.setObjectName(_fromUtf8("closePB"))
        self.gridLayout_3.addWidget(self.closePB, 0, 4, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DecaRangeRTLS", None))
        self.label.setText(_translate("MainWindow", "串口号:", None))
        self.openPB.setText(_translate("MainWindow", "打开串口", None))
        self.closePB.setText(_translate("MainWindow", "关闭串口", None))

