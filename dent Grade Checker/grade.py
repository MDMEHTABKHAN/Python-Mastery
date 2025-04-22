name = input("Enter your name: ")

subject1 = int(input("Enter marks for Math: "))
subject2 = int(input("Enter marks for Science: "))
subject3 = int(input("Enter marks for English: "))

total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3

passed_all_subjects = subject1 >= 35 and subject2 >= 35 and subject3 >= 35

print("\nStudent Name:", name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

if passed_all_subjects:
    print("Result: PASSED")
else:
    print("Result: FAILED")
