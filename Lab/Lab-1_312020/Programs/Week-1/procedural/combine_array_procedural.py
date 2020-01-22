#8) Given a two list of ints create a third list such that should contain only odd numbers from the first list and even numbers from the second list

def combine ():

    s1= int(input("Enter array 1 size: "))
    ar1= []
    for _ in range(s1):
        ar1.append(int(input()))
    
    s2= int(input("Enter array 2 size: "))
    ar2= []
    for i in range(s2):
        ar2.append(int(input()))
    ar3 = []
    for i in ar1:
        if i%2 != 0:
            ar3.append(i)
    for j in ar2:
        if j%2==0:
            ar3.append(j)
    print("list:",ar3)
    
combine()