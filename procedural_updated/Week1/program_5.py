# 5.Write a program that prompts the user to enter an integer for today�s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6).
# Also prompt the user to enter the number of days after today for a future day and display the future day of the week. 

def dayfinder(dk):
    switcher={
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    print(switcher.get(dk,"Invalid Day"))

day = int(input("Enter Number: "))
dk = day%7

dayfinder(dk)

k = input("Want to check for more dates[Y/N]: ")

while k == 'Y' or k == 'y':
    day = int(input("Enter Number: "))
    dk = day%7

    dayfinder(dk)
    k = input("Want to check for more dates[Y/N]: ")

