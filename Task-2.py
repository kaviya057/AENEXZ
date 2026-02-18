#Write a function that takes the radius of a circle and returns its area.
import math
def circle(r):
    return math.pi*r*r 
radius=int(input("enter radius to find area of a circle: "))
result=circle(radius)
print(result)