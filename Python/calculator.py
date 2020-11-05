#Calculator
#Written by Lukas

a = int(input("Enter your first number"))
b = int(input("Enter your second number"))

def doMath(a,b,c):
    answer = 0
    if(c==1):
        answer = a+b
    if(c==2):
        answer = a-b
    if(c==3):
        answer = a*b
    if(c==4):
        answer = round(a/b,2)
    if(c==5):
        answer = a%b
    return str(answer)

print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))


        
