import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)

while True:
    GPIO.output(23,1)
    time.sleep(1)
    GPIO.output(23,0)

