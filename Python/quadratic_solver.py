
def rootFinder(a,b,c):
    discriminant = b**2 - 4*a*c
    roots = []
    
    if discriminant < 0:
        return str("There are no real roots")
    elif discriminant >= 0:
        root1 = (-b + discriminant**.5)/2*a
        root2 = (-b - discriminant**.5)/2*a
        roots.append(root1)
        roots.append(root2)
        return roots


a = int(input("enter the coefficient of your x^2 term: "))
b = int(input("enter the coefficient of your x term: "))
c = int(input("enter the value of your numerical term: "))


print(rootFinder(a,b,c))
