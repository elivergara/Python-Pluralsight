class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Name must be provided")

        self.name = name
        self.house = house


    def __str__(self):
        return f'{self.name} from {self.house}'
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError('not a valid house')
        self._house = house
        

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)



if __name__ == "__main__":
    main()



