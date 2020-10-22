# Automatic Dice Roller
# written by Lukas

from random import randint

print ("Automatic Dice Roller")
go = True

while go:
	i = str(input("Click enter to roll dice and x to leave:"))
	if i == "":
		print(randint(1,6))
	elif i == "x":
		print("exiting apllication")
		go = False
