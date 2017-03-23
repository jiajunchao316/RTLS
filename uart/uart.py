# -*- coding: cp936 -*-
'串口类及相关操作文件'
import serial.tools.list_ports
from algorithm.Myalgorithm import JiSuan
from threading import Thread

class SerachCK(Thread):
    '''搜索串口'''
    def __init__(self,MW):
        Thread.__init__(self)
        self.mw = MW
        self.preckNum = 0
        self.prelistCK = []

    def run(self):
        while True:
            self.listCK = []
            self.chaneglis = []
            ckNum = len(list(serial.tools.list_ports.comports()))
            if ckNum == self.preckNum:
                continue
            else:
                for i in xrange(ckNum):
                   self.listCK.append(list(serial.tools.list_ports.comports())[i][0])
                self.listCK = set(self.listCK)
                if ckNum > self.preckNum:
                    for x in self.listCK:
                        if x not in self.prelistCK:
                           self.chaneglis.append(x)
                    self.mw.CKcomboBox.addItems(self.chaneglis)
                            
                elif ckNum < self.preckNum:
                    self.mw.CKcomboBox.clear()
                    self.mw.CKcomboBox.addItems(self.listCK)

                self.preckNum = ckNum
                self.prelistCK = self.listCK


class MySerial(object):
    '''串口类'''
    def __init__(self,mw,act,ms):

        self.ser = serial.Serial()
        self.going = False
        self.mw = mw
        self.act = act
        self.ms = ms
        self.CKN = ''

        self.rck = ReadCK(self.ser)
        self.rck.setDaemon(True)
        self.rck.start()

        self.js = JiSuan(self.ser,self.rck,self.act,self.ms)
        self.js.setDaemon(True)
        self.js.start()

    def selectCK(self,CKnum):
        self.CKN = CKnum

    def openCK(self):
        if self.ser.isOpen():
            pass
        else:
            if self.CKN == '':
                cknum = self.mw.CKcomboBox.itemText(0)
            else:
                cknum = self.CKN
            if cknum == '':
                print 'CAN NOT FOUND ANY COM'
                pass
            else:
                self.ser.port = str(cknum)
                self.ser.baudrate = 115200
                self.ser.open()
                print 'open'
             
    def closeCK(self):
        if self.ser.isOpen():
            self.ser.close()
            print 'close'
        
class ReadCK(Thread):
    '''读串口'''
    def __init__(self,ser):
        Thread.__init__(self)
        self.ser = ser

        self.head_f = ''
        self.head_s = ''
        self.head_t = ''
        self.list_R = []
        self.p1 = []
        self.p2 = []
        self.p3 = []
        self.flag_f = True
        self.flag_s = True
        self.flag_t = True

    def hex2dec(self,data):
        return int(data.upper(),16)

    def run(self):
        while True:
            if self.ser.isOpen():
                try:
                    data = self.ser.readline(self.ser.inWaiting())
                except:
                    continue

                if (data[0:2] == 'ma') and self.flag_f is True:
                    self.flag_f = False
                    self.head_f = data[0:4]
                    try:
                        r1 = float(self.hex2dec(data[9:17]))/1000
                    except:
                        pass
                    continue

                if (data[0:2] == 'ma') and self.flag_s is True:
                    self.flag_s = False
                    self.head_s = data[0:4]
                    if self.head_s != self.head_f:
                        try:
                            r2 = float(self.hex2dec(data[9:17]))/1000
                        except:
                            pass
                    continue

                if (data[0:2] == 'ma') and self.flag_t is True:
                    self.flag_t = False
                    self.head_t = data[0:4]
                    if self.head_t != self.head_s and self.head_t != self.head_f:
                        try:
                            r3 = float(self.hex2dec(data[9:17]))/1000
                            self.list_R = [r1,r2,r3]
                        except:
                            pass

                self.flag_f = True
                self.flag_s = True
                self.flag_t = True
                #print self.list_R
