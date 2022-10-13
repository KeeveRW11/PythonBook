# from tkinter import Y

# x = 1
# y = 2

# x = input("Whats x? ")
# y = input("Whats y? ")

# z = int(x) + int(y)

# x = int(input("Whats x? "))
# y = int(input("Whats y? "))

# x = float(input("Whats x? "))
# y = float(input("Whats y? "))

#ROUND TO TWO DECIMAL PLACES
# z = round(x / y, 2)
# print(z)

#OR
# z = x / y
# print(f"{z:.2f}")


# print(x + y)

#FORMAT A NUMBER USING AN F STRING
#z = round(x + y)
# print(z)
# print(f"{z:,}")

# DEFINE A FUNCTION
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n        

main()    
