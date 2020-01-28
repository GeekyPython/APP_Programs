#1.Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
def age_input():
    global name
    global age
    name = input("Enter Your Name:")
    age = int(input("Enter Your Age: "))

def age_output():
    print(name, " will be 100 years old at", 2120-age)

name = " "
age = 0
age_input()
age_output()
