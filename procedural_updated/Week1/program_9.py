# 9) Return the number of times that the string �Emma� appears anywhere in the given string

def substr(statement):
   count1 = 0
   count2 = 0
   for i in range(len(statement)-1):
       count1 += statement[i:i+4] == 'Emma'
   for i in range(len(statement)-1):
       count2 += statement[i:i+4] == 'emma'
   count = count1 + count2
   print("Emma appeared ", count, "times")

st = input("Enter String: ")
print("Input String:", st)
st
substr(st)