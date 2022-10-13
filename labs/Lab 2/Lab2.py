# Our aim in this lab was to calculate the 'x' using the quadratic formula.
# Getting a random integer for a
# Getting a random for b with rounding the number to 2 decimal point
# Asking for input for the c co-efficient 
#Calculating the x using the quadratic formula

import math
import random

a = random.randint(1,10)
print("a is ",a)
b = round(random.uniform(0, 10), 2)
print("b is ",b)
c = float(input("Enter c: "))
c = math.copysign(c, -0.0)
print("c is ",c)

print(a,"x^2 +" , b , "x +" , c ,"= 0")

x_1 = (-b + math.sqrt(b**2 - (4*a*c)))/(2*a)
x_2 = (-b - math.sqrt(b**2 - (4*a*c)))/(2*a)

print("x = ",x_1, "and" , x_2)
