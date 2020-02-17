#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

class SoloSensor(object):


    def __init__(self,Soil):
        self.soil = Soil

    def medir(self):
        GPIO.setmode(GPIO.BCM)
        channel = self.soil
        GPIO.setup(channel, GPIO.IN)
        retorno = False
        if(GPIO.input(channel) == GPIO.LOW):
            retorno = True
        return retorno

if __name__ == '__main__':
    try:
        c = SoloSensor(18) 
        print(c.medir())
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        print("Finally Soil")

