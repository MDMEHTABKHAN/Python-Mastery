# Creating a list
my_list = [1, 2, 3, 4, 5]

# Adding elements
my_list.append(6)          # [1, 2, 3, 4, 5, 6]
my_list.extend([7, 8])     # [1, 2, 3, 4, 5, 6, 7, 8]
my_list.insert(0, 0)       # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Removing elements
my_list.remove(0)          # [1, 2, 3, 4, 5, 6, 7, 8]
my_list.pop()              # [1, 2, 3, 4, 5, 6, 7]
my_list.clear()            # []

# Searching and Counting
my_list = [1, 2, 3, 4, 5, 2]
index = my_list.index(2)   # 1
count = my_list.count(2)   # 2

# Sorting and Reversing
my_list.sort()             # [1, 2, 2, 3, 4, 5]
my_list.reverse()          # [5, 4, 3, 2, 2, 1]

# Copying
new_list = my_list.copy()  # [5, 4, 3, 2, 2, 1]