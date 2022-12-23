import re

# name = input("What's your name? ").strip()

# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")

name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#ABOVE CAN BE WRITTEN AS - using Walrus Operator
if matches := re.search(r"^(.+), (.+)$", name):
    # last = matches.group(1)
    # first = matches.group(2)
    # # last, first = matches.group()
    # name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
