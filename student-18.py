# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house


#     def __str__(self):
#         return f'{self.name} from {self.house}'
    
#     @property
#     def house(self):
#         return self._house
    
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, name):
#         if not name.strip():
#             raise ValueError('not a valid name')
#         self._name = name
        
#     @house.setter
#     def house(self, house):
#         if house not in ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]:
#             raise ValueError('not a valid house')
#         self._house = house
        

# def main():
#     student = get_student()
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)



# if __name__ == "__main__":
#     main()



from tabulate import tabulate


def main():
    print("\nTaskMaster | To-Do List")
    running = True
    database, count = [], 0

    while running:
        action = get_input()

        if action == "V":
            view(database)
        elif action == "C":
            database, count = create(database, count)
        elif action == "U":
            database = update(database)
        elif action == "D":
            database = delete(database)
        else:
            running = False


def get_input():
    instructions = [{"Key": "V", "Action": "View Tasks"},
                    {"Key": "C", "Action": "Create a Task"},
                    {"Key": "U", "Action": "Update a Task"},
                    {"Key": "D", "Action": "Delete a Task"},
                    {"Key": "E", "Action": "Exit"}]

    while True:
        print(tabulate(instructions, headers="keys", tablefmt="rounded_outline"))
        action = input("What do you want to do?: ").upper()

        if action in ["V", "C", "U", "D", "E"]:
            return action
        else:
            print("Invalid key, try again.")


def view(data):
    print(tabulate(data, headers="keys", tablefmt="rounded_grid"))


def create(data, i):
    task, i = input("Task: "), i + 1
    data.append({"ID": i, "Task": task})
    return data, i


def update(data):
    numbers = list(task["ID"] for task in data)

    while True:
        view(data)
        try:
            i = int(input("Which task would you like to update?: "))
            if i in numbers:
                break
            else:
                print("Invalid task ID, try again.")

        except ValueError:
            print("Invalid input, try again.")

    new = input("What do you want to update it to?: ")
    for task in data:
        if task["ID"] == i:
            task["Task"] = new

    return data


def delete(data):
    numbers = list(task["ID"] for task in data)

    while True:
        view(data)
        try:
            i = int(input("Which task would you like to delete?: "))
            if i in numbers:
                break
            else:
                print("Invalid task ID, try again.")

        except ValueError:
            print("Invalid input, try again.")

    for j in range(len(data)):
        if data[j]["ID"] == i:
            del data[j]
            break

    return data


if __name__ == "__main__":
    main()