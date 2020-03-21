list1 = [1, 3, 4, 6, 8] 
list2 = [4, 5, 6, 2, 10] 
ilist = [4, 2, 8, 3, 2, 1]

print ("Original list 1 : " + str(list1)) 
print ("Original list 2 : " + str(list2)) 
print("Input list : " +str(ilist))

temp_list = list(map(lambda x,y:x+y, list1, list2)) 
res_list = list(map(lambda x,y:x*y, temp_list, ilist))

print("Sum of list 1, 2: " +str(temp_list))
print ("Final list after multiplication list is : " + str(res_list)) 