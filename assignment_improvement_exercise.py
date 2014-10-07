#john bain
#variable improvement exercise
#05-09-12

import math
radius = int (input("please enter the radius of the circle: "))
circumference = 2* math.pi * radius
circumference = round(circumference,2)
answer = int (math.pi * radius**2)
answer = round(answer,2)
print("The circumference of this circle is {0}.".format(circumference))
print("The area of this circle is {0}.".format(answer))
