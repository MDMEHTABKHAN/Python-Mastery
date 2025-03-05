fruits = {"apple", "banana", "cherry"}

# Removes "banana"; raises an error if not found
fruits.remove("banana")

# Removes "cherry"; does NOT raise an error if not found
fruits.discard("cherry")
print(fruits)

# Removes and returns a random element
removed_item = fruits.pop()
print(removed_item)

fruits.clear()  # Removes all elements
print(fruits)  # Output: set()



