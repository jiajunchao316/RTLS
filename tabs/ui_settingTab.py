# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingTab.ui'
#
# Created: Tue Oct 27 20:19:42 2015
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

class Ui_setTab(object):
    def setupUi(self, setTab):
        setTab.setObjectName(_fromUtf8("setTab"))
        setTab.resize(252, 443)
        self.gridLayout = QtGui.QGridLayout(setTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(setTab)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.checkBox_Trackking_2 = QtGui.QCheckBox(self.tab_1)
        self.checkBox_Trackking_2.setObjectName(_fromUtf8("checkBox_Trackking_2"))
        self.gridLayout_2.addWidget(self.checkBox_Trackking_2, 0, 0, 1, 1)
        self.checkBox_Geo = QtGui.QCheckBox(self.tab_1)
        self.checkBox_Geo.setObjectName(_fromUtf8("checkBox_Geo"))
        self.gridLayout_2.addWidget(self.checkBox_Geo, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.tab_1)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox.setEnabled(True)
        self.doubleSpinBox.setReadOnly(False)
        self.doubleSpinBox.setKeyboardTracking(True)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.tab_1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_2.setReadOnly(False)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radioButton_Out = QtGui.QRadioButton(self.tab_1)
        self.radioButton_Out.setObjectName(_fromUtf8("radioButton_Out"))
        self.horizontalLayout_4.addWidget(self.radioButton_Out)
        self.radioButton_In = QtGui.QRadioButton(self.tab_1)
        self.radioButton_In.setObjectName(_fromUtf8("radioButton_In"))
        self.horizontalLayout_4.addWidget(self.radioButton_In)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.checkBox_ShowTag = QtGui.QCheckBox(self.tab_1)
        self.checkBox_ShowTag.setObjectName(_fromUtf8("checkBox_ShowTag"))
        self.horizontalLayout_3.addWidget(self.checkBox_ShowTag)
        self.spinBox = QtGui.QSpinBox(self.tab_1)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_3.addWidget(self.spinBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)
        self.checkBox_ShowTagTab = QtGui.QCheckBox(self.tab_1)
        self.checkBox_ShowTagTab.setObjectName(_fromUtf8("checkBox_ShowTagTab"))
        self.gridLayout_2.addWidget(self.checkBox_ShowTagTab, 6, 0, 1, 1)
        self.checkBox_ShowAncTab = QtGui.QCheckBox(self.tab_1)
        self.checkBox_ShowAncTab.setObjectName(_fromUtf8("checkBox_ShowAncTab"))
        self.gridLayout_2.addWidget(self.checkBox_ShowAncTab, 7, 0, 1, 1)
        self.checkBox_ShowCorTab = QtGui.QCheckBox(self.tab_1)
        self.checkBox_ShowCorTab.setObjectName(_fromUtf8("checkBox_ShowCorTab"))
        self.gridLayout_2.addWidget(self.checkBox_ShowCorTab, 8, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.horizontalLayout_5.addWidget(self.doubleSpinBox_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 0, 1, 2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.checkBox_ShowGrid = QtGui.QCheckBox(self.tab_3)
        self.checkBox_ShowGrid.setObjectName(_fromUtf8("checkBox_ShowGrid"))
        self.gridLayout_3.addWidget(self.checkBox_ShowGrid, 3, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 268, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 4, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(setTab)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(setTab)

    def retranslateUi(self, setTab):
        setTab.setWindowTitle(_translate("setTab", "Form", None))
        self.checkBox_Trackking_2.setText(_translate("setTab", "Tracking/Navigation", None))
        self.checkBox_Geo.setText(_translate("setTab", "Geo-Fencing Mod", None))
        self.label.setText(_translate("setTab", "Zone  1  (m)", None))
        self.label_2.setText(_translate("setTab", "Zone  2  (m)", None))
        self.radioButton_Out.setText(_translate("setTab", "Alare Outside", None))
        self.radioButton_In.setText(_translate("setTab", "Alare Inside", None))
        self.checkBox_ShowTag.setText(_translate("setTab", "Show Tag Histor", None))
        self.checkBox_ShowTagTab.setText(_translate("setTab", "Show Tag Tab", None))
        self.checkBox_ShowAncTab.setText(_translate("setTab", "Show Anchor Tab", None))
        self.checkBox_ShowCorTab.setText(_translate("setTab", "Show Anc-Tag Correction Tab", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("setTab", "Configuration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("setTab", "Floor Flan", None))
        self.label_3.setText(_translate("setTab", "Width (m)", None))
        self.label_4.setText(_translate("setTab", "Height (m)", None))
        self.checkBox_ShowGrid.setText(_translate("setTab", "Show Grid", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("setTab", "Grid", None))
