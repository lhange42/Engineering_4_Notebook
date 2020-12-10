import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)

while True:
    print("working")
    GPIO.output(3,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(3,GPIO.LOW)
    time.sleep(1)
