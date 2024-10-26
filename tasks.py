import argparse
import os

class ToDoList:
    def __init__(self, filename="todo_list.txt"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return [line.strip() for line in file.readlines()]
        return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {task}")
    
    def del_task(self, task):
        self.tasks.remove(task)
        self.save_tasks()
        print(f"Task removed: {task}")
        print(f"remaining tasks:\n")
        self.list_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Current tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

def main():
    # Create an instance of ArgumentParser
    parser = argparse.ArgumentParser(description="A simple to-do list program.")
    
    # Add arguments for adding a task or listing tasks
    parser.add_argument('--add', type=str, help="Add a task to the to-do list")
    parser.add_argument('--delete', type=str, help="Remove a task from the to-do list")
    parser.add_argument('--list', action='store_true', help="List all tasks")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Create an instance of ToDoList
    todo = ToDoList()
    
    # Handle the arguments
    if args.add:
        todo.add_task(args.add)

    if args.delete:
        todo.del_task(args.delete)
    
    if args.list:
        todo.list_tasks()

if __name__ == "__main__":
    main()
