# Take input from the user
marks = int(input("Enter the marks: "))

if 90 <= marks <= 100:
    print("Excellent")
elif 80 <= marks <= 89:
    print("Very Good")
elif 70 <= marks <= 79:
    print("Good")
elif 60 <= marks <= 69:
    print("Average")
else:
    print("Poor")


