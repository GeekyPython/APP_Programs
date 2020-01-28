num = int(input("enter number of number in first list: "))
print("enter first list:")
myl1 = []
for i in range(0,num):
  r=int(input())
  myl1.append(r)
num = int(input("enter number of number in second list: "))
print("enter second list:")
myl2 = []
for i in range(0,num):
  r=int(input())
  myl2.append(r)
print("list1:",myl1)
print("list2:",myl2)
myl3 = []
for i in myl1:
    if i%2!=0:
        myl3.append(i)
for j in myl2:
    if j%2==0:
        myl3.append(j)
print("final list:",myl3)