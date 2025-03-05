my_list = [10, 20, 30, 40, 50]

# Modifying elements
my_list[1] = 200  # Change the second element to 200
print(my_list)    # Output: [10, 200, 30, 40, 50]

# Adding elements
my_list.append(60)  # Add 60 to the end
print(my_list)      # Output: [10, 200, 30, 40, 50, 60]

# Inserting elements
my_list.insert(2, 300)  # Insert 300 at index 2
print(my_list)          # Output: [10, 200, 300, 30, 40, 50, 60]

# Removing elements
my_list.remove(200)  # Remove the first occurrence of 200
print(my_list)       # Output: [10, 300, 30, 40, 50, 60]

# Deleting elements by index
del my_list[1]       # Remove element at index 1
print(my_list)       # Output: [10, 30, 40, 50, 60]