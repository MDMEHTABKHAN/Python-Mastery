# positional arguments
# def power_of(a,b):
#     c = a ** b
#     print(c)
# power_of(2,5)
# power_of(5,2)
# power_of(2,4)
# power_of(2,3)

# default arguments
# def power_of(a, b = 5):
#     c = a ** b
#     print(c)
# power_of(2,5)
# power_of(3)

def sum_of_two_number(x = 20, y = 10):
    sum = x + y
    print(sum)
sum_of_two_number()    

sum_of_two_number(23)
sum_of_two_number(0, 1)


# keyword arguments

def mul(a, b):
    c = a * b
    print(c)
mul(a = 3, b = 4)
mul(a = 2, b = 3)
mul(b = 5, a = 10) 