company = {
    "employee1": {"name": "John", "age": 30, "role": "Developer"},
    "employee2": {"name": "Doe", "age": 25, "role": "Designer"}
}

# Accessing nested dictionary
print(company["employee1"]["name"])


student = {
    "name": "Mehtab",
    "age": 24,
    "course": "Computer Science",
    "skills": ["Python", "SQL", "MySQl", "PostgreSQL"]
}


# Adding a new key-value pair
student["city"] = "Hyderabad"

# Removing a key-value pair using del
# del student["course"]

# print(student)


# Iterating through keys
for key in student:
    print(key, ":", student[key])

# iterating through key value pair
for key, value in student.items():
    print(f"{key}: {value}")