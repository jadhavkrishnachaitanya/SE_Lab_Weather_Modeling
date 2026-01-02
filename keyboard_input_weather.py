import math

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = b*b - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are:", x1, x2)
elif d == 0:
    x = -b / (2*a)
    print("Root is:", x)
else:
    print("No real roots")
