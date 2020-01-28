count = 0
for i in range(100,1001):
    if(i%5==0 and i%6==0):
        print(i,end=" ")
        count = count + 1
        if(count//10>0):
            count = count - 10
            print("\n")