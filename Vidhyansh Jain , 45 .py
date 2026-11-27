

n = int(input("Enter number of students: "))

total_class = 0

for i in range(1, n + 1):
    total = 0

    print("Enter marks for Student", i)

    for j in range(1, 6):
        marks = float(input("Test " + str(j) + ": "))
        total += marks

    average = total / 5
    total_class += average

    print("Average of Student", i, "=", average)

overall_average = total_class / n

print("Overall Average =", overall_average)
