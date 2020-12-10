import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)# powers that pin

while True:
    print("working")
    GPIO.output(3,GPIO.HIGH)# turns the LED off
    time.sleep(1)# waits 1 second
    GPIO.output(3,GPIO.LOW)# turns the LED off
    time.sleep(1)# waits 1 second
