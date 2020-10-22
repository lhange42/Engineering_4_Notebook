# Automatic Dice Roller
# written by Lukas

from random import randint

print ("Automatic Dice Roller") 
go = True # Makes the condition of the while wloop true allowing it to run

while go:
	i = str(input("Click enter to roll dice and x to leave:")) # prints this message after every dice roll
	if i == "":
		print(randint(1,6)) # This prints a random int from 1 to 6
	elif i == "x":
		print("exiting apllication")
		go = False # this else if reads if x then enter was clicked so then it makes go false and stops the loop
