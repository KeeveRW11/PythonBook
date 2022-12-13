# with open("students.csv") as file:
#     for line in file:
#         #ADDING ONE VARIABLE PUTS EVERY THING IN ONE 
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")

# with open("students.csv") as file:
#     for line in file:
#         #CAN ADD TO TWO SEPARATE VARIABLES WITH USE OF COMMA
#         name, house = line.rstrip().split(",")
#         # print(f"{name[0]} is in {house[1]}")
#         print(f"{name} is in {house}")

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         # students.append(f"{name} is in {house}")
# # #SORT BY NAME
# # for student in sorted(students):
# #     print(student)
#         # student = {}
#         # student["name"] = name
#         # student["house"] = house
#         # students.append(student)
#         #MORE COMPACT
#         student = {"name": name, "house": house}
#         students.append(student)

# # def get_name(student):        
# #     return student["name"]
# # # SINGLE QUOTES NEEDED INSIDE
# # # passing functions as arguments
# # for student in sorted(students, key=get_name):
# #     print(f"{student['name']} is in {student['house']}")
# # def get_name(student):        
# #     return student["name"]
# # SINGLE QUOTES NEEDED INSIDE
# # passing LAMBDA functions as arguments
# for student in sorted(students, key=lambda student:student["name"]):
#     print(f"{student['name']} is in {student['house']}")
# import csv

# students = []
# #CSV Reader
# # with open("students.csv") as file:
# #         reader = csv.reader(file)
# #         for row in reader:
# #             students.append({"name": row[0], "home": row[1]})
# #DictReader
# with open("students.csv") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key=lambda student:student["name"]):
#     print(f"{student['name']} is from {student['home']}")
import csv 

name = input ("What's your name? ")
home = input ("Where's your home? ")

# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})