import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)
print("LAMPADA LIGADA\n")
GPIO.output(11, GPIO.LOW)
time.sleep(2)
print("LAMPADA DESLIGADA\n")
GPIO.output(11, GPIO.HIGH)

#print(GPIO.output(11,state))
