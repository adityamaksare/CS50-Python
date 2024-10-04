# Dict: Keys on the left and values on the right
students = {
    "Hermione":"Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor"
}

# Accessing the values using keys in the dictionary
print(students["Hermione"])

# Accessing both, keys and values
for student in students:
    print(student, students[student], sep=", ")
