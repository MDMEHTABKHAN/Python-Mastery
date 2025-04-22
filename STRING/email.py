def is_valid_email(email):
    if "@" in email and "." in email:
        return "Valid email"
    else:
        return "Invalid email"

email = input("Enter an email: ")
print(is_valid_email(email))
