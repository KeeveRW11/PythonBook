# students = ["Hermione", "Harry", "Ron"]
# use square numbers to get the item in the index. index starts at 0
# print(students[0])
# print(students[1])
# print(students[2])

# for student in students:
#     print(student)

# LEN
# for i in range(len(students)):
#     print(i + 1, students[i])

#DICTIONARIES
# houses ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
# In the case below, each name represents a key and the left is a value
# dictionaries unlike list allows you to use the key instead of an integer

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# # print(students["Harry"])
# for student in students:
#     print(student, students[student], sep=", ")

# List of Dictionaries
#None is a keyword for null
students = [
    {"name":"Hermione", "house": "Gryffindor", "patronous": "Otter"},
    {"name":"Harry", "house": "Gryffindor", "patronous": "Stag"},
    {"name":"Ron", "house": "Gryffindor", "patronous": "Jack Russell Terrier"},
    {"name":"Draco", "house": "Slytherin", "patronous": None}
]
for student in students:
    print(student["name"], student["house"], student["patronous"], sep=", ")