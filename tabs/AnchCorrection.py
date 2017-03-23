# -*- coding: cp936 -*-
from PyQt4 import QtCore, QtGui
from ui_AnchCorrection import Ui_AnchTab
from draw.draw import GraphWidget,MS
import sys
import numpy as np

class AnchTab(QtGui.QWidget):
    '''参考节点表格'''
    def __init__(self,gw):
        super(AnchTab,self).__init__()
        self.ui = Ui_AnchTab()
        self.ui.setupUi(self)
        self.gw = gw
        self.listbp = []

        self.settings = QtCore.QSettings('RTLS','ACT')
        self.bp = self.settings.value('list_bp',type=float)
        self.row = self.settings.value('int_row',type=int)

        if self.row:
            self.ui.tableWidget.setRowCount(self.row)
        else:
            self.ui.tableWidget.setRowCount(4)

        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setColumnWidth(0,63)
        
        for i in range(self.ui.tableWidget.columnCount()):
            self.ui.tableWidget.setColumnWidth(i+1,58)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['Anc ID','X(m)','Y(m)','Z(m)'])

        for i in range(self.ui.tableWidget.rowCount()):
            newItem = QtGui.QTableWidgetItem('  %d' % i)
            self.ui.tableWidget.setItem(i,0,newItem)
            newItem.setFlags(QtCore.Qt.ItemIsEnabled)

        if self.bp:
            self.bp = np.array(self.bp).reshape(self.row,3)
            self.listbp = self.bp
            for x in range(self.row):
                for y in range(3):
                    data = QtGui.QTableWidgetItem('%0.3f'%self.bp[x][y])
                    self.ui.tableWidget.setItem(x,y+1,data)    

        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.setAlternatingRowColors(True)
        self.ui.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        #self.connect(self.ui.tableWidget,QtCore.SIGNAL('cellChanged (int,int)'),self.sendBP)
        self.ui.savebpPB.clicked.connect(self.GetBP)

    def GetBP(self):
        self.listbp = []
        row = self.ui.tableWidget.rowCount()
        col = self.ui.tableWidget.columnCount()-1
        try:
            for x in range(row):
                for y in range(col):
                    self.listbp.append(float(QtCore.QString('%1').arg(
                        self.ui.tableWidget.item(x,y+1).text().toFloat()[0])))
            self.settings.setValue('int_row',row)
            self.settings.setValue('list_bp',self.listbp)
            self.listbp = np.array(self.listbp).reshape(self.row,3)
            msList = [MS() for i in range(self.row)]
            for i in xrange(len(msList)):
                ms = msList[i]
                ms.setcolor(0,128,192)
                self.gw.additem(ms)
                ms.setPos(20*i,50)
                
        except:
            QtGui.QMessageBox.warning(self,'warning',u'节点坐标错误')
                
        
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    Anch = AnchTab()
    Anch.show()
    sys.exit(app.exec_())

