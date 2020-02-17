import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.IN)

for i in range(0,5):
        print GPIO.input(3)

GPIO.cleanup();        
