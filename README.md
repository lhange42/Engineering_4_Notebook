# Engineering_4_Notebook
My Engineering 4 notebook


## Hello Python 

### Description 
  In this assignment we make a python code that if you click enter gives you a random number 1 to 6 and if you click x and enter it quits the application

### Lessons Learned 
  In this assignment I reacquainted myself with python commands and terminal commands. Like how you end functions with colon's and that strings are str. I also learned that else ifs are elif. I learned that nano is how to edit a file and if you only have reading access you can use sudo nano. I learned that "python3 file name" runs the code in that file. Also during my creation of the the file I miss named it so I also learned that using "rm file name" you can remove files.

### Images and Links
<img src="Images/Hello_Python-Lukas.png" width="400">
 

## Calculator

### Description
  In this assignment we make a python code that asks for two integers to be inputted by the user.
    
### Lessons Learned 
  In this assignment I learned how to def functions by using "def function name():" and any parameters you need you can put in the parantheses. I also learned that the round function is simply just "round(math function, number of digits to round)". Also I learned that I had to return my integer answer as a string to print it. 
  
### Images and Links
<img src="Images/Calculator-Lukas.png" width="400">

## Quadratic Solver

### Description
  In this assignment we make a code that finds out if there are roots of a quadratic with 3 user inputted coefficients and if there are roots it finds them and puts them into an array and prints them. 
    
### Lessons Learned 
  In this assignment I learned how to make a array/list by setting a variable = []. I learned the command variable.append(number) this adds a number or string to the list at the end. I learned that the ** is the math operator for an exponent. I also learned the raspberry pi command sudo shutdown -h now which will shut down the raspberry pi.
### Images and Links
<img src="Images/Quadratic_Solver-Lukas.png" width="400">


## Strings and Loops

### Description
  In this assignment we make a code that gets a user inputted sentence that gets turned into a list by characters and printed one by one
    
### Lessons Learned 
  In this assignment I learned how to replace certain parts of a string using string.replace("whatever I want replaced", "what I want to replace it"). I also learned setting a string equal to a list by doing string = list(string) will make it list seperated by letter.
### Images and Links
<img src="Images/Loops_and_Strings-Lukas.png" width="400">

## MSP(Hangman)

### Description
  This assignment is to create a hangman program which prompts for a user inputted word then prints something out for every wrong letter guess.
    
### Lessons Learned 
  In this assignment I used a lot of similar commands from previous mainly involving a lot of lists. I learned the way to open and read text files in python which var = (file_name.txt, "r") then var.read() will read the file. I also learned to enumerate to keep track of all instances of a guess in the word that is being guessed using enumerate(list). I aslo learned "".join(list) which when put in print function will turn a list into a string when using quotations. I already knew this but it's the first time I've used it this year in coding so I thought I'd include that the break command simply ends a loop and simply requires typing the word break wherever in a loop you want it to break.
### Images and Links
<img src="Images/Hangman_Win-Lukas.png" width="400">
<img src="Images/Hangman_Loss-Lukas.png" width="400">

## SSH LED Blinking

### Description
  In this assignment we connect to our pi to our computer using the wifi by getting our pi's ip address and since I'm on computer I used Secure Shell
  
### Lessons Learned 
  In this assignment I learned how to turn my pi's ssh on "sudo raspi-config" and going to interface options and SSH. I also learned that how you connect is simply making the username pi since that's your login for the pi and the hostname is the ip address. I've used these before but time.sleep(how long you want to wait) is how you wait.
  
### Images and Links
<img src="Images/SSH_LED_Wiring.png" width="400">


## I2C

### Description
  in this [assignment](https://github.com/lhange42/Engineering_4_Notebook/blob/main/Python/I2C.py) I had to use an accelerometer and a OLED display to display the changing acceleration of x,y, and z values using I2C to transfer the data from the accelerometer to the display. 
  
### Lessons Learned 
  I learned a lot of new things in this assignment. I learned a lot of new display commands. The example codes were actually really helpful for learning commands and seeing the different functions I can use. Also in the assignment is shows that the accelerometer returns six values since it includes a magnetometer so you have to set up a variable just to hold those mag values so you can seperate them. 
  
### Images and Links
<img src="Images/I2C-Lukas.png" width="400">


## Headless

### Description
  in this [assignment](https://github.com/lhange42/Engineering_4_Notebook/blob/main/Python/Headless.py) I had to use my acceleromter and OLED display but now to make some kind of visual displaying one of the accelerations and get the to automatically happen on the pis boot up without you running the code directly.
  
### Lessons Learned 
  In this assignment I learned a couple new things not many new commands though since it's very similar to I2C. 
  
### Images and Links
<img src="Images/" width="400">
This [link](https://www.youtube.com/watch?v=Ivj7ueXaRsI&feature=youtu.be) is a video showing the OLED Display graph. The change is hard to see because of the little amount of acceleration by me simply moving the accelerometer back and forth but still shows the scatter plot being made. 

## Bash

### Description
   In this [assignment](https://github.com/lhange42/Engineering_4_Notebook/blob/main/Python/bash.sh) we used bash to make two leds blink
  
### Lessons Learned 
  I learned how to use bash and a few commands. I learned that echo is the command to print. I learned you need #!/bin/bash at the start of a bash script. Also to be able to run a bash script you need to chmod +x file name to be able to run it. To do rests you simply type sleep put a space then just put the time wanted. I also learned for loops which you can see how to do in my code.

## Flask Hello World

### Description
  in this [assignment](https://github.com/lhange42/Engineering_4_Notebook/blob/main/Python/Flash/hello_world/app.py)  
  
### Lessons Learned 
 
  
### Images and Links
<img src="Images/Hello_World_Flask-Lukas.png" width="400">
