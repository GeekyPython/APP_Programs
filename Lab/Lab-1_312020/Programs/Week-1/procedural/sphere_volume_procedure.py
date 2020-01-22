#4. Write a Python program to get the volume of a sphere with radius 

import math as m

def vol_calc(rad):
    v = (4/3)*m.pi*m.pow(rad, 3)
    print("Volume of sphere is: ", '%.3f'%v)

def inp():
    global rad
    rad = float(input("Enter Radius: "))

rad = 0
inp()
vol_calc(rad)