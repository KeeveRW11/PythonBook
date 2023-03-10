# Object-Oriented Programming
# Classes - Instance Methods

class Student:
    # indent block as seen below is needed for class attributes if we are not using the __init__ method
    # ...

    # Methods - below we see the dunder init method - this defines the objects of the class
    # self is a reference to the object itself - it needs to be the first argument - self assigns the attributes to the object
    def __init__(self, name, house):

        if not name:
            # raise an exception
            raise ValueError("Name cannot be empty.")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError(f"Invalid house {house}")    
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    # call the student class
    # student = Student()
    # # call the prompt method - use the . operator to access the method
    # student.name = input("Name: ")
    # student.house = input("House: ")

    # return the student object without using the . operator
    # pass arguments to the class
    name = input("Name: ")
    house = input("House: ")
    # below we see a constructor - creates an object of the class - in this case the student object
    student = Student(name, house)


    # return the student object
    return student


if __name__ == "__main__":
    main()

  