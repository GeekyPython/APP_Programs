number_of_students = int(input("\nEnter the number of students:"))

# set the student 'Nobody' just for clarity
current_student = ("Nobody", 0)

first_place = [current_student]
second_place = [current_student]

while number_of_students > 0:
    name = input("\nEnter student's name: ")
    score = input("\nEnter student's score: ")

    if not name or not score:
        break

    score = int(score)
    current_student = (name, score)

    # retrieve the two highest scorers from lists
    first_score = first_place[0][1]
    second_score = second_place[0][1]

    if score > first_score:
        second_place = first_place
        first_place= [current_student]

    elif score == first_score:
        first_place.append(current_student)

    elif score > second_score:
        second_place = [current_student]

    elif score == second_score:
        second_place.append(current_student)

    number_of_students-=1


print("\n\nFirst place")
for name, score in first_place:
    print(name, score, end=" ")

print("\n\nSecond place")
for name, score in second_place:
    print(name, score, end=" ")

print("\n")