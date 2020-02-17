# -*- coding: utf-8 -*-
#########################################################
# Rele no BCM 14, positivo de 5v
#
#
########################################################
#import requests
import datetime
import time
import os
import sys
import json
sys.path.insert(1,'/home/pi/Sensores/reles')
sys.path.insert(1,'/home/pi/Sensores/DS18B20')
from myRele import MyRele
from myDS18B20 import myDS18B20

class Estufa(object):

    def __init__(self):
        self.rele = MyRele(14)
        self.releCobra = MyRele(18)
        self.check = self.rele.check()
        self.checkCobra = self.releCobra.check()
        print(self.rele.check())
        if 'desliga' in sys.argv:
           self.rele.off()
           self.releCobra.off()
        elif 'liga' in sys.argv:
            self.rele.on()
            self.releCobra.on()
        self.verificaRele()
        self.verificaReleCobra()

    def verificaRele(self):
        da = datetime.datetime.now()
        hora_x = int(da.strftime('%H%M'))
        print(datetime.datetime.now())
        if hora_x > 600 and hora_x < 2330:
            if self.check == 1:
                self.rele.on()
            print("Rele 1 ligado")
        else:
            if self.check == 0:
                self.rele.off()
            print("Rele 1 desligado")


    def verificaReleCobra(self):
        DS = myDS18B20()
        temp = DS.read_temp()
        da = datetime.datetime.now()
        hora_x = int(da.strftime('%H%M'))
        print(temp)
        if temp < 29:
            if self.checkCobra == 1:
                self.rele.on()
            print("Rele cobra ligado")
        else:
            if self.checkCobra == 0:
                self.rele.off()
            print("Rele cobra desligado")



if __name__ == '__main__':
    Estufa()
