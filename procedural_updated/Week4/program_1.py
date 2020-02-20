def doubler(a):
    return a*2

def function():
    s= int(input("Enter Size of list:"))
    l=[]
    for _ in range(0,s):
        l.append(int(input("Enter Element: ")))
    print(list(map(doubler,l)))

function()