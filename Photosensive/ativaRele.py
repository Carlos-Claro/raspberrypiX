import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.OUT)
#GPIO.setup(3,GPIO.OUT)

for i in range(0,5):
    time.sleep(5);
#    ativo = GPIO.input(0)
    print i
    if( i % 2 == 0 ):
        GPIO.output(15,GPIO.HIGH)
    GPIO.output(15,GPIO.LOW)   
GPIO.cleanup()    
