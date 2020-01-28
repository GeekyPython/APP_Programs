statement=input("enter string: ")
count1 = 0
count2 = 0
for i in range(len(statement)-1):
        count1 += statement[i:i+4] == 'Emma'
for i in range(len(statement)-1):
        count2 += statement[i:i+4] == 'emma'
count = count1 + count2
print("Emma appeared ", count, "times")