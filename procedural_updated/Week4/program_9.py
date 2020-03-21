
F =[]
C= []
x=1
while x== 1:
    foc = input("Enter F for Fahrenheit to Celcius (or) enter C for Celcius to Fahrenheit: ")
    if foc =="F":
        F.append(float(input("Enter temprature: ")))
        x= int(input("Press 1 to enter more: "))
        if x !=1:
            break
    elif foc =="C":
        C.append(float(input("Enter temprature: ")))
        x= int(input("Press 1 to enter more: "))
        if x !=1:
            break
    else:
        break

print("Entered Fahrenheit list: ", F, "\nEntered Celcius list: ", C)

C2F= list(map(lambda x: ((9/5*x)+32),C))
F2C= list(map(lambda x: ((x-32)*5/9),F))

print("Fahrenheit converted to Celcius: ",round(F2C),"\nCelcius converted to Farenheit: ", round(C2F))