# 14.(Find numbers divisible by 5 and 6) Write a program that displays, ten numbers per line, all the numbers from 100 to 1,000 that are divisible by 5 and 6. The numbers are separated
#    by exactly one space. (hint : use loop and lambda )

def div_56():
    count = 0
    for i in range(100,1001):
        if(i%5==0 and i%6==0):
            print(i,end=" ")
            count = count + 1
        if(count/10 ==0):
            count = count - 10
            print('\n')


div_56()