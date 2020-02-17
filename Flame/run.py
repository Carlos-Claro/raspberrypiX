import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN)#Right sensor connection
while True:
    i=GPIO.input(15)                         #Reading output of right IR sensor
    if i==0:                                #Right IR sensor detects an object
        print "chama detectada"
        time.sleep(0.1)
    else :
        print "Tranquilo"
        time.sleep(0.1)

