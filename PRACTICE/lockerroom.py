users = {
    'Mehtab': 1234,
    'Shyam': 36534,
    'abdul': 32544,
    'Amit': 2435
}

# Ask for user input
name = input('Enter your name: ')
pin = int(input('Enter your PIN: '))

# Check if the user exists
if name in users:
    if users[name] == pin:
        print(f'Access granted. Welcome, {name}!')
    else:
        print('Incorrect PIN. Access denied.')
else:
    print('User not recognized. Access denied.')

