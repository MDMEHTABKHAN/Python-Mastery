# Swap Two Numbers Without Using a Third Variable 
a = int(input("Enter the first number: ")) 
b = int(input("Enter the second number: ")) 
a = a + b 
b = a - b 
a = a - b 
print("After swapping, first number:", a)
print("After swapping, second number:", b) 