def calculate_average(score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    return average

num_students = int(input("How many students? "))

for i in range(num_students):
    print("Student", i + 1)

    name = input("Enter name: ")
    score1 = float(input("Activity 1: "))
    score2 = float(input("Activity 2: "))
    score3 = float(input("Activity 3: "))

    average = calculate_average(score1, score2, score3)

    if average >= 90 and average <= 100:
        status = "Excellent"
    elif average >= 80 and average <= 89:
        status = "Very Good"
    elif average >= 75 and average < 79:
        status = "Passed"
    else:
        status = "Failed"

    print("Name:", name)
    print("Activity 1:", score1)
    print("Activity 2:", score2)
    print("Activity 3:", score3)
    print("Average:", round(average, 2))
    print("Status:", status)

print("All students done!")