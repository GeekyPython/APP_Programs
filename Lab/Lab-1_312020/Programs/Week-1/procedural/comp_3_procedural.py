#Write a program that prompts the user to enter three integers and displays them in increasing order. (using if..elif structure)

def compare():
    a= int(input("Enter first element: "))
    b= int(input("Enter second element: "))
    c= int(input("Enter third element: "))
    
    if (a>=b) and (a>=c):
        print("Numbers in increasing order is:\n", a)
        if(b>=c):
            print(b)
            print(c)
        else:
            print(c)
            print(b)
        
    elif (b>=a) and (b>=c):
        print("Numbers in increasing order is:\n", b)
        if(a>=c):
            print(a)
            print(c)
        else:
            print(c)
            print(b)
    else:
        print("Number in increasing order is:", a," ", b, " ",c)

compare()