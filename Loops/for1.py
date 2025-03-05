txt = 'String'

for items in txt:
    print(items)

lst1 = [10,20,30,40,50,60,70,80,90,100]

# for i in lst1:
#     print(i)

# number = int(input('enetr number: '))
# for i in range(10):
#     print(i)  

# n = int(input("Enter a number: "))
# sum_n = n * (n + 1) // 2
# print(f"Sum of first {n} natural numbers is: {sum_n}")


# m = int(input("Enter a number: "))
# sum_m = 0
# for i in range(1, m + 1):
#     sum_m += i
# print(f"Sum of first {m} natural numbers is: {sum_m}")



for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i = {i}, j = {j}")

