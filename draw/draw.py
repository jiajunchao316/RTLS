# -*- coding: cp936 -*-
'地图及相关绘制'
from PyQt4 import QtCore, QtGui
from threading import Thread
import math

class GraphWidget(QtGui.QGraphicsView):
    '''绘图操作'''
    def __init__(self,ms):
        super(GraphWidget, self).__init__()

        self.scene = QtGui.QGraphicsScene()
        self.scene.setItemIndexMethod(QtGui.QGraphicsScene.NoIndex)
        self.scene.setSceneRect(-500, -500, 1000, 1000)
        self.setScene(self.scene)
        self.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        self.setCacheMode(QtGui.QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QtGui.QGraphicsView.FullViewportUpdate)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setTransformationAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtGui.QGraphicsView.AnchorViewCenter)

        tilePixmap = QtGui.QPixmap(100, 100)
        tilePixmap.fill(QtCore.Qt.white)
        tilePainter = QtGui.QPainter(tilePixmap)
        color = QtGui.QColor(220, 220, 220)
        tilePainter.fillRect(0, 0, 50, 50, color)
        tilePainter.fillRect(50, 50, 50, 50, color)
        tilePainter.end()
        self.setBackgroundBrush(QtGui.QBrush(tilePixmap))

        self.adjust_x = -200
        self.adjust_y = -200


        self.ms = ms
        self.additem(self.ms)
        self.ms.setPos(25+self.adjust_x,-25+self.adjust_y)

    def additem(self,ms):
        self.scene.addItem(ms)

    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_Up:
            self.centerNode.moveBy(0, -20)
        elif key == QtCore.Qt.Key_Down:
            self.centerNode.moveBy(0, 20)
        elif key == QtCore.Qt.Key_Left:
            self.centerNode.moveBy(-20, 0)
        elif key == QtCore.Qt.Key_Right:
            self.centerNode.moveBy(20, 0)
        elif key == QtCore.Qt.Key_Plus:
            self.scaleView(1.2)
        elif key == QtCore.Qt.Key_Minus:
            self.scaleView(1 / 1.2)
        elif key == QtCore.Qt.Key_Space or key == QtCore.Qt.Key_Enter:
            for item in self.scene().items():
                if isinstance(item, Node):
                    item.setPos(-150 + QtCore.qrand() % 300, -150 + QtCore.qrand() % 300)
        else:
            super(GraphWidget, self).keyPressEvent(event)

    def wheelEvent(self, event):
        self.scaleView(math.pow(2.0, event.delta() / 240.0))


    
    def scaleView(self, scaleFactor):
        factor = self.matrix().scale(scaleFactor, scaleFactor).mapRect(QtCore.QRectF(0, 0, 1, 1)).width()

        if factor < 0.7 or factor > 10:
            return

        self.scale(scaleFactor, scaleFactor)


class MS(QtGui.QGraphicsItem):
    '''绘制移动节点'''
    BoundingRect = QtCore.QRectF(-10-2, -10-2, 20+2, 20+2)

    def __init__(self):
        super(MS, self).__init__()
        self.color = QtGui.QColor(240,140,0)

    def setcolor(self,r,g,b):
        self.color = QtGui.QColor(r,g,b)
   
    def boundingRect(self):
        return self.BoundingRect

    def shape(self):
        path = QtGui.QPainterPath()
        path.addEllipse(-10, -10, 20, 20)
        return path

    def paint(self, painter, option, widget):

        painter.setBrush(self.color)
        painter.setPen(QtGui.QPen(QtCore.Qt.darkYellow, 0))
        painter.drawEllipse(-10, -10, 20, 20)
        
  
