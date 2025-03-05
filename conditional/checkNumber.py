num = int(input('Enter a number: '))

if num > 0 and num % 2 == 0:
    print('Positive even number')
elif num > 0 and num % 2 != 0:
    print('Positive odd number')    
else:
    print('Negative number')