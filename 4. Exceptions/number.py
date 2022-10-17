# x = int(input("Whats x? "))

# print(f"x is {x}")
# INVALID ERROR
#     x = int(input("Whats x? "))
# ValueError: invalid literal for int() with base 10: '3.142'


#try and except
# try:
#     x = int(input("Whats x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

# Whats x? 1.1 or try cat
# x is not an integer

#NAME ERROR
#nameError: name 'x' is not defined
#else
# try:
#     x = int(input("Whats x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

#REPROMPTING
# Use a while loop
# while True:
#     try:
#         x = int(input("Whats x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")

#GET_INT
# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break # a break only breaks a loop
#     return x #return is stronger than break. It will break out of a function and a loop

# main()

#PASS
# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             pass

# main()

#FUNCTION ARGUMENT
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            pass

main()