# names = []

# for _ in range(3):
#     # name = input("What's your name? ")
#     names.append(input("What's your name? "))
#     # print(f"hello, {name}")
# for name in sorted(names):
#     print(f"hello, {name}")

# SAVE IN LIST USING FILE I/O

name = input("What's your name? ")

# use open function - "w" means write. In this example we assign to file.
# "w" will overwrite content each time
# file = open("names.txt", "w")
# Use "a" append to add and save to list
# file = open("names.txt", "a")
# # Writes to the file
# file.write(f"{name}\n")
# dont have to use close
# file.close() 
# do this instead
with open("names.txt", "a") as file:
    # Writes to the file. ensure to indent.
    file.write(f"{name}\n")
