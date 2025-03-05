# Using parentheses
my_tuple = (1, 2, 3)

# Using the tuple constructor
another_tuple = tuple([4, 5, 6])

# Single-element tuple (note the trailing comma)
single_element_tuple = (1,)

# Empty tuple
empty_tuple = ()

num = (1)
print(type(num), num) # int

mixed_tuple = (12, 45.56, 'txt', True)
print(mixed_tuple)


# convert list to tuple
l = [1,23,45]
tpl = tuple(l)
print(tpl, type(tpl)) # tuple



# Define the tuple
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(t, type(t))  # tuple

# Convert the tuple to a list
lst = list(t)
print(lst, type(lst))  # list
