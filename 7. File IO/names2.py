# with open("names.txt", "r") as file:
# #     lines = file.readlines()
# # for line in lines:
# #     print("hello,", line.strip())
# # we use strip to remove the space between lines
#     for line in file:
#         print("hello,", line.rstrip())

# SORT

# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"hello, {name}")

# # SAME AS ABOVE BUT MORE COMPACT
# with open("names.txt") as file:
#     for line in sorted(file):
#        print(f"hello, {name}")

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
# We can reverse the sorted with reverse set to True
for name in sorted(names, reverse=True):
    print(f"hello, {name}")