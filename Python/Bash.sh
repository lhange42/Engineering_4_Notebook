#!/bin/bash

for i in {1..20} #turns it on and off 10 times by toggling it 20 times
do
	/usr/bin/gpio -1 toggle 27   #toggles gpio pin 27 on and off
	sleep .5  #to make sure the led is on and off for solid amount of time
done
