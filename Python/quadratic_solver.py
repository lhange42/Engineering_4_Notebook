def rootFinder(a,b,c):
    discriminant = b**2 - 4*a*c #determines if the inside of the quadratics square root is positive or negative determining if the roots are real
    roots = []# creates the array
    
    if discriminant < 0:# if the discriminant is negative
        roots.append("There are no real roots")#makes the list contain a string  
    elif discriminant >= 0:# reads if the discriminant is positive
        root1 = (-b + discriminant**.5)/(2*a)# solves for the root in which the top of the quadratic is adding
        root2 = (-b - discriminant**.5)/(2*a)# solves for the root in which the top of the quadratic is subtracting
        roots.append(root1)# adds the first root to the array
        roots.append(root2)# adds the second root to the array
    return roots# returns the roots array to where the rootFinder function was called

a = int(input("enter the coefficient of your x^2 term: "))# These variables provide 3 user integer inputs that will become the coefficients of the quadratics
b = int(input("enter the coefficient of your x term: "))
c = int(input("enter the value of your numerical term: "))

print(rootFinder(a,b,c))# prints the outcome of the root function as an array 
