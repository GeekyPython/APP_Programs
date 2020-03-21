def cube(v): 
    return v*v*v

x= int(input("Enter a number: "))

print("From def() : " +str(cube(x)))
c = lambda x: x*x*x
print("From lambda : "+ str(c(x)))