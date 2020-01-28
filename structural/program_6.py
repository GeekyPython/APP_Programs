num=int(input("enter:"))
n = num
rem = 0
new = 0
while(n>0):
    rem = n%10
    new = new*10 + rem
    n = n//10
if new==num:
    print("The reverse number is as same as the original number")
else:
    print("The reverse and the original number are not the same")