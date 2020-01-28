print("Sunday=0\nMonday=1\nTuesday=2\nWednesday=3\nThursday=4\nFriday=5\nSaturday=6")
day=int(input("enter the day(in number): "))
num=int(input("the number of days to be add: "))
su = day + num
di = su%7
if di==0:
    print("\nSunday")
elif di==1:
    print("\nMonday")
elif di==2:
    print("\nTuesday")
elif di==3:
    print("\nWednesday")
elif di==4:
    print("\nThursday")
elif di==5:
    print("\nFriday")
else:
    print("\nSaturday")