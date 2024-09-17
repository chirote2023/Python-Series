# area = pi*r**2
# circumference = 2*pi*r

import math

def circle(radius):
    area = math.pi *radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a,c = circle(4)

print("Area : ", a, "Circumference : ",c)