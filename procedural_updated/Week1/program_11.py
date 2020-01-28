# 11.(Financial application: compute future tuition) Suppose that the tuition for a university is $10,000 this year and increases 5% every year. Write a program that computes the 
#    tuition in ten years and the total cost of four years� worth of tuition starting ten years from now.

def calc():
    x= float(input("Enter tution fees: $"))

    for i in range(0,10,1):
        x= x + x*0.05
        if i == 3:
            k = x
    
    print("In 10 years the tution fees will be  : $", round(x,2))
    print ("In 4 years the tution fees will be  : $", round(k,2))

calc()