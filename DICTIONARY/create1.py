student1 = {
    "name": "Mehtab",
    "age": 23,
    "hobbies":["cricket", "football", "cooking"],
    "student1": {
        "name": "Shyam",
        "age": 27,
    },
}

# print(student1)


student = {
    "name": "Mehtab",         # String
    "age": 23,                # Integer
    "height": 5.9,            # Float
    "is_student": True,       # Boolean
    "hobbies": ["cricket", "football", "cooking"],  # List
    "skills": ("Python", "SQL"),  # Tuple
    "marks": {90, 85, 88},    # Set
    "details": {              # Nested Dictionary
        "address":"IBP",
        "PIN": 501506
    }
}

# print(student)

print(student["hobbies"][0])
print(student["details"]["address"])

print(student["marks"])



