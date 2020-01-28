#6) Print the following pattern
#1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5

def pattern_printer():
    num = 1
    n = 5
    for i in range (0,n):
        for i in range (0, i+1):
            print(num, end= " ")
        num= num +1
        print("\r")

pattern_printer()