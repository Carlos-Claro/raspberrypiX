import serial
import json
comunicacao = serial.Serial('/dev/ttyUSB0',9600)
try:
    a = comunicacao.readline()
    print(a)
    #v = {}
    #v['humidade'] = 80.0
    #v['temperatura'] = 22.2
    #print(json.dumps(v))
    b = json.loads(a)
    print(b)
except (OSError, serial.SerialException):
    print(serial.SerialException)
    pass

