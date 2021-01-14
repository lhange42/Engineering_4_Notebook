# Bash
# Lukas Hange
#!/bin/bash


for i in {1..20} # for loop that runs 20 times
do	
	
	/usr/bin/gpio toggle 29 # this toggles gpio26 on and off
	sleep .5	
done
