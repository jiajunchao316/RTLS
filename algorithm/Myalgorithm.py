# -*- coding: cp936 -*-
import serial
from math import*
import numpy as np
from threading import Thread


p1 = np.array([0.8,1.2,0.2])
p2 = np.array([1.8,12.9,0.75])
p3 = np.array([6.6,11.8,0.8])     
class JiSuan(Thread):
    '''计算移动节点坐标'''
    def __init__(self,ser,rck,act,ms):
        Thread.__init__(self)
        self.ser = ser
        self.rck = rck
        self.act = act
        self.ms = ms
        self.count = 0
        self.adx = 0
        self.ady = 0

        print self.act.listbp

    def run(self):
        while True:
            if self.ser.isOpen():
                if len(self.rck.list_R) == 3:
                    self.count = self.count + 1
                    r1 = self.rck.list_R[0]
                    r2 = self.rck.list_R[1]
                    r3 = self.rck.list_R[2]

                    hh = sqrt(np.dot(p2-p1,p2-p1))
                    ex = (p2-p1)/hh
                    t1 = p3-p1
                    ii = np.dot(ex,t1)
                    t2 = ii*ex
                    ey = (t1-t2)/sqrt(np.dot(t2-t1,t2-t1))
                    jj = np.dot(ey,(p3-p1))
                                                
                    x = (r1**2 - r2**2)/(2*hh) + hh/2
                    y = (r1**2 - r3**2 + ii**2)/(2*jj) + jj/2 - x*ii/jj
                    z = r1**2 - x**2 - y**2
                    if z < 0: 
                        z = abs(z)

                    result = p1+x*ex+y*ey

                    px = float(('%0.3f' % result[0]))
                    py = float(('%0.3f' % result[1]))

                    self.adx = self.adx + px
                    self.ady = self.ady + py

                    print px,py

                    if self.count == 5:
                        msx = float('%0.1f' % self.adx)/5.0
                        msy = float('%0.1f' % self.ady)/5.0
                        print msx,msy
                        self.ms.setPos(50*msx,50*msy)
                        self.count = 0
                        self.adx = 0
                        self.ady = 0

                    
