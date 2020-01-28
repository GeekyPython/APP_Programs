#7) Reverse a given number and return true if it is the same as the original number

def reverse(s): 
	return s[::-1] 

def isPalindrome(s): 

	rev = reverse(s) 

	if (s == rev): 
		return True
	return False


s = input("Enter number: ")
ans = isPalindrome(s) 

if ans == 1: 
	print("Yes") 
else: 
	print("No") 