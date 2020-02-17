#! /usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(10, gpio.IN, pull_up_down = gpio.PUD_DOWN)

while True:
    if(gpio.input(10) == 1):
        print("Botao pressionado")
    else:
        print("Botao desligado")
    time.sleep(2)

gpio.cleanup()
exit()
