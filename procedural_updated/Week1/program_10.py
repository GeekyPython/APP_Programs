#10.Write a program that reads an unspecified number of integers, determines how many positive and negative values have been read, and computes the total and average of the input
 #values (not counting zeros). Your program ends with the input 0. Display the average as a floating-point number. Here is a sample run:

def printer():
    print("Enter numbers to increment the counter, loop ends once input is 0")
    num= int(input())
    cp = 0
    cn = 0
    while num != 0 :
        if num >0 :
            cp = cp + 1
        else:
            cn= cn + 1
        num= int(input())
    avg = float((cp+cn)/2)
    print ("average of +ve and -ve is: ", avg)
printer()