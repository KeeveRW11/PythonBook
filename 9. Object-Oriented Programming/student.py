# Object-Oriented Programming
# Tuples
def main():
    # name = input("Name: ")
    # house = input("House: ")
    
    # name = get_name()
    # house = get_house()

    # return tuple value as student - use square brackets to index into the tuple
    # student = get_student()
    # # print(f"{name} from {house}")

    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"

    # print(f"{student[0]} from {student[1]}")

    # for Dictionary
    student = get_student()

    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    
    #use the key to index into the dictionary - ensure to use single quotes around the keys
    print(f"{student['name']} from {student['house']}")


# def get_name():
#     return input("Name: ")
    
# def get_house():
#     return input("House: ")

def get_student():
    # name = input("Name: ")
    # house = input("House: ")

    # # return a tuple (tuple ar immutable, cannot be changed)
    # # return name, house

    # # returns a list (list can be changed) - use square brackets to index into the list - separate by commas
    # return [name, house]

    # Dictionaries - key-value pairs 
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

    # Alternative way to create a dictionary
    # name = input("Name: ")
    # house = input("House: ")
    # return {"name": name, "house": house}

if __name__ == "__main__":
    main()

  