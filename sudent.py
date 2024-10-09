# Define a class called 'Student'. A class is a blueprint for creating objects that have certain properties and methods.
""" How It Works:
When you run the code, the main() function is executed.
- It asks the user for the student's information (name, house, and patronus).
- Then it creates a Student object with that information and 
- prints it using the __str__ method.
"""
class Student:
    
    # This is the constructor method, called when an instance (object) of the class is created.
    # It is used to initialize the object with specific data (name, house, patronus).
    def __init__(self, name, house, patronus):
        
        # Check if the 'name' parameter is empty. If it is, raise an error.
        # This ensures that every student has a name.
        if not name:
            raise ValueError('Name cannot be empty')
        
        # Check if the provided 'house' is valid. The house must be one of the four Hogwarts houses.
        # If the house is not valid, raise an error. This ensures the student is assigned to a proper house.
        if house not in  ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw']:
            raise ValueError(f"{house} is not a valid house")
        
        # Assign the 'name', 'house', and 'patronus' attributes to the student object.
        # 'self' is used to refer to the instance of the class.
        self.name = name
        self.house = house
        self.patronus = patronus

    # Define a method called '__str__'. This is a special method that returns a string representation of the object.
    # When we try to print the student object, this method is called to provide a meaningful output.
    def __str__(self):
        return f"Student: {self.name}, from House: {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐎"
            case "Otter":
                return "🦦"
            case "Jack Russell":
                return "🐕"
            case _:
                return "🪄"


# Define a function called 'main' that serves as the starting point of the program.
def main():
    # Call the 'get_student' function to create a new student and store it in the 'student' variable.
    student = get_student()
    
    # Print the student object. This automatically calls the '__str__' method of the 'Student' class.
    print("Expecto Patronum!")
    print(student.charm())

# Define a function called 'get_student' that collects information about a student from the user.
def get_student():
    # Prompt the user to enter the student's name and store it in the 'name' variable.
    name = input("Name: ")
    
    # Prompt the user to enter the student's house and store it in the 'house' variable.
    house = input('House: ')
    
    # Prompt the user to enter the student's patronus and store it in the 'patronus' variable.
    patronus = input("Patronus: ")
    
    # Create a new 'Student' object using the collected information and return it.
    return Student(name, house, patronus)
    
# Call the 'main' function to run the program.
main()
