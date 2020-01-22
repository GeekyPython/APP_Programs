#3. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them  
def inp():
    global st_in
    st_in= input("Enter your first name and last name: ")

def out(st_in):
    print(st_in[::-1])

st_in = "NULL"

inp()
out(st_in)