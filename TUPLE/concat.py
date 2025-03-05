tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)



# repetition
my_tuple = (1, 2)
repeated = my_tuple * 3 


# memebership
my_tuple = (1, 2, 3, 4, 5)
exists = 3 in my_tuple
print(exists)

exists1 = 6 in my_tuple
print(exists1)

exists2 = 6 not in my_tuple
print(exists2)


tup = (10,20,30,40,50,60,70,80,90,100)
print(len(tup))

# min and max
min_value = min(tup)  
max_value = max(tup)
print(min_value)
print(max_value)

# sum
print(sum(tup))