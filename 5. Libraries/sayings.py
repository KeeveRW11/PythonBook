def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

#best way to use main function is to     
if __name__ == "__main__":
    main()
#the conditional will ignore the main and only call the function being imported in the other file