####################################
#http://www.quemdevnaoteme.com/
# negativo + 100 Ohm
# board 12 out
# 2019-02-02
#
#
####################################
import RPi.GPIO as GPIO
import time

# Configuracao da placa
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

# Loop
try:
    while True:
        GPIO.output(12, 1)
        print("a")
        time.sleep(1)
        GPIO.output(12, 0)
        print("b")
        time.sleep(1)

except KeyboardInterrupt:
    pass

# Limpa as configuracoes
GPIO.cleanup()

