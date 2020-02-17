import os
import glob
import time
from datetime import datetime
import RPi.GPIO as GPIO


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    print(lines)
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    time.sleep(0.2)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        if  temp_c > 30.1: 
            GPIO.output(17,GPIO.HIGH)
            print("Rele Desligado")
            print(temp_c);
        else :    
            GPIO.output(17,GPIO.LOW)
            print("rele Ligado")
            print(temp_c)
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
#while True:
now = datetime.now()
print(now)
print(read_temp())
time.sleep(10)
print(read_temp())
time.sleep(10)
print(read_temp())
time.sleep(10)
print(read_temp())
time.sleep(10)
print(read_temp())
#GPIO.cleanup()
