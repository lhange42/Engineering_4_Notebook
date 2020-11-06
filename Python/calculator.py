#Calculator
#Written by Lukas

a = int(input("Enter your first number"))# gets a user input as an integer 
b = int(input("Enter your second number"))# gets a user input as an integer

def doMath(a,b,c):# Defines a function with three parameters
    answer = 0 # is the variable answer that I will return to print
    if(c==1): # if the parameter c is 1 you add
        answer = a+b #adds the first inputted value to the second inputted value
    if(c==2):# if the parameter c is 2 you subtract
        answer = a-b# subtracts the inputted values by each other
    if(c==3):# if the parameter is 3 you multiply
        answer = a*b#multiplies the inputted values by each other
    if(c==4):# if the parameter c is 4 you divide
        answer = round(a/b,2)# divides the inputted values and rounds them to 2 digits
    if(c==5):# if the parameter c is 5 you modulos and find the remainder
        answer = a%b# finds the remainde of the division of the inputted numbers
    return str(answer)# returns the answer as a string of whateber math function was preformed

print("Sum:\t\t" + doMath(a,b,1))# these all print each function of math
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))


        
