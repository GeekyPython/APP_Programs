# 13.(Find the two highest scores) Write a program that prompts the user to enter the number of students and each student�s score, and displays the highest and secondhighest scores. 

def high_2():
    score = []
    score.append(input("Enter First Score: "))
    k = input("Enter more Score[Y/N]: ")
    while k == 'Y' or k == 'y':
        score.append(input("Enter Next Score: "))
        k = input("Enter more Score[Y/N]: ")

    score.sort()
    length = len(score)
    print("The highest score and the 2nd highest scores are: ", score[length-1], score[length-2])

high_2()