import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) #just gets rid of weird warnings
leds = [15, 16] #sets up a list that contains the two pins for the LED
GPIO.setmode(GPIO.BOARD)# makes the gpio pins identified by their board values instead of BCM values
GPIO.setup(leds, GPIO.OUT) # makes the pins output 

for i in range(0, 10): # makes a for loop that runs ten times
	GPIO.output(leds, 1)# makes the leds turn on
	time.sleep(0.5)# time delay 
	GPIO.output(leds, 0)# makes the leds turn off
	time.sleep(0.5)# time delay
