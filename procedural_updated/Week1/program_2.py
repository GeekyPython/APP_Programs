#2.Write a Python program which accepts the radius of a circle from the user and compute the area.�
#Sample Output :�r = 1.1Area = 3.8013271108436504                

import math

def rad_calc(rad):
    v= math.pi*rad*rad
    print("Area of circle of", rad, "is", v)

def inp():
    global rad
    rad = float(input("Enter Radius: "))

rad = 0
inp()
rad_calc(rad)