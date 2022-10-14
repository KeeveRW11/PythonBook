#WHILE LOOP

# This is not DRY - do not repeat yourself
# print("meow")
# print("meow")
# print("meow")

# i = 0
# while i < 3:
#     print("meow")
#     i += 1

#FOR LOOP  - allows to iterate over a list of items

# for i in [0, 1, 2]:
#     print("meow")

#Use function range instead of writing out a full list
# for i in range(3):
#     print("meow")


#    \n will create a new line & the end= will determine where the breaks end
# print("meow\n" * 3, end="")

# INFINITE LOOP - When you want to get user input that matches what you want
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#     #     continue
#     # else:
#         break

# for _ in range(n):
#     print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
       n = int(input("What's n? "))
       if n > 0:
            break
    return n     

def meow(n):
    for _ in range(n):
        print("meow")

main()
