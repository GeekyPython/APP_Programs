#  15.Write a program that reads an integer and displays all its smallest factors, also known as prime factors. For example, if the input integer is 120, the output should be as
#     follows: 2, 2, 2, 3, 5

import math as m

def factor():
    n = int(input("Enter Your Input for prime factor: "))
    while n%2 == 0:
        print(2, end=',')
        n =n/2
    for i in range (3,int(m.sqrt(n))+1,2):
        while n%i ==0:
            print(i,end= ',')
            n= n/i
    if n>2 :
        print(n)

factor()