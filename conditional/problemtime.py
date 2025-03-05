current_time = int(input("Enter the current time (in hours, 0-23): "))

# Determine the time of day using if, elif, and else

if 5 <= current_time <= 11:
    print("Good morning")
elif 12 <= current_time <= 16:
    print("Good afternoon")
elif 17 <= current_time <= 20:
    print("Good evening")
else:
    print("Good night")
