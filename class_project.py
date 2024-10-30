###############################################################
# CS50P: Introduction to Programming with Python - Harvard University
# Final Project: Digital Recipe Book
# Author: Eli Vergara
# Date: October 28-2024
# Description:
# This program is a digital recipe book that allows multiple users to create, store, edit, and print recipes. 
# It includes features such as:
#   - User authentication to enable personalized recipe storage per user.
#   - The ability to create, view, update, and delete recipes.
# Purpose:
# This was a request from my wife as she wants to have a way to to organize her recipes.
#
# Requirements:
# Python 3 or above (this was made using 3.12)
# Additional libraries: [csv, os, tabulate, and textwrap which helps to display the table], 
# Next steps: I am learning tkinter and I want to make a gui as I continue to learn how to use it.
################################################################
import csv
import os
import getpass
import textwrap
from tabulate import tabulate
from pyfiglet import Figlet

f = Figlet(font='small')
data_file = 'users.csv'

def main_menu():
    """ Initiate the program asking the ruser to register or to enter the program"""
    print(f.renderText("Welcome to your digital Recipe Book"))
    while True:  
        print("\nMain Menu\n")
        try:
            num = int(input("Select from the following options:\n 1 to register a new user \n 2 to enter the program: "))
            if num == 1:
                create_user()  
                print(f"New user registered successfully!\n")
            elif num == 2:
                print("Please Login to proceed.")
                if user_login():  
                    return  
            else:
                print("You must enter 1 or 2")  
        except ValueError:
            print("You must enter 1 or 2") 

def create_user():
    """Creates new username and password, and creates a recipes file for the newly registered user."""
    register_user = input("Enter a username: ").lower().strip()
    register_pwd = getpass.getpass(f"Enter a password for {register_user}: ").strip()

    with open("users.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["user", "password"])
        writer.writerow({"user": register_user, "password": register_pwd})

    user_recipe_file = f"{register_user}.csv"
    with open(user_recipe_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Meal Category", "Dish Name", "Ingredients", "Cooking Directions"])

    global users_data
    users_data = load_users()

def load_users():
    """Load users from a CSV file and return a dictionary of username: password."""
    users = {}
    if os.path.exists(data_file):
        with open(data_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:  
                    username, password = row
                    users[username] = password
    return users

users_data = load_users()

def user_login():
    """Authenticate user login and proceed to recipes menu."""
    login_attempts = 0
    while login_attempts < 3:
        username = input("Enter your User Name: ").lower().strip()
        password = getpass.getpass("Enter your password: ").strip()
        
        if username in users_data and users_data[username] == password:
            print(f.renderText(f"{username}'s recipes!"))
            recipes_menu(username) 
            return True 
        else:
            login_attempts += 1 
            attempts_left = 3 - login_attempts
            print(f"Invalid username or password!\n{attempts_left} attempts left. Please try again.")
    return False

class Recipes:
    """Class to manage recipes for each user."""
    def __init__(self, username):
        self.username = username
        self.filename = f"{self.username}.csv"
        self.load_recipes()

    def load_recipes(self):
        """Load recipes from the user's CSV file."""
        self.recipes = []
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.recipes.append(row)

    def add_recipe(self):
        """Add a new recipe to the user's collection."""
        category = input("Enter Meal Category: ").strip()
        name = input("Enter Dish Name: ").strip()
        ingredients = input("Enter Ingredients (comma-separated): ").strip()
        directions = input("Enter Cooking Directions: ").strip()
        recipe = {"Meal Category": category, "Dish Name": name, "Ingredients": ingredients, "Cooking Directions": directions}
        self.recipes.append(recipe)
        self.save_recipes()
        print("Recipe added successfully!")

    def edit_recipe(self):
        """Edit an existing recipe."""
        self.print_recipes()
        choice = int(input("Enter the number of the recipe to edit: ")) - 1
        if 0 <= choice < len(self.recipes):
            recipe = self.recipes[choice]
            recipe['Meal Category'] = input(f"Enter new Meal Category (current: {recipe['Meal Category']}): ").strip() or recipe['Meal Category']
            recipe['Dish Name'] = input(f"Enter new Dish Name (current: {recipe['Dish Name']}): ").strip() or recipe['Dish Name']
            recipe['Ingredients'] = input(f"Enter new Ingredients (current: {recipe['Ingredients']}): ").strip() or recipe['Ingredients']
            recipe['Cooking Directions'] = input(f"Enter new Cooking Directions (current: {recipe['Cooking Directions']}): ").strip() or recipe['Cooking Directions']
            self.save_recipes()
            print("Recipe updated successfully!")
        else:
            print("Invalid choice. Returning to menu.")

    def delete_recipe(self):
        """Delete a recipe from the user's collection."""
        self.print_recipes()
        choice = int(input("Enter the number of the recipe to delete: ")) - 1
        if 0 <= choice < len(self.recipes):
            del self.recipes[choice]
            self.save_recipes()
            print("Recipe deleted successfully!")
        else:
            print("Invalid choice. Returning to menu.")

    def print_recipes(self):
        """Display all recipes for the user in a tabular format with numbering and wrapped text."""
        if self.recipes:
            print(f"\nMy Recipes:")
            headers = ["No.", "Meal Category", "Dish Name", "Ingredients", "Cooking Directions"]
            rows = []
            for idx, recipe in enumerate(self.recipes, start=1):
                # Wrap the "Cooking Directions" to a specified width
                wrapped_directions = "\n".join(textwrap.wrap(recipe.get("Cooking Directions", ""), width=40))  # Adjust width as needed
                row = [idx, recipe.get("Meal Category", ""), recipe.get("Dish Name", ""),
                    recipe.get("Ingredients", ""), wrapped_directions]
                rows.append(row)
            print(tabulate(rows, headers=headers, tablefmt="grid"))
        else:
            print("No recipes found.")


    def save_recipes(self):
        """Save recipes back to the CSV file."""
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Meal Category", "Dish Name", "Ingredients", "Cooking Directions"])
            writer.writeheader()
            writer.writerows(self.recipes)

def recipes_menu(username):
    """Displays the recipe management menu for a logged-in user."""
    user_recipes = Recipes(username)  # Initialize Recipes for the logged-in user
    while True:
        print(f"\nSelect an option:\n 1 - Add New Recipe\n 2 - Edit Existing Recipe\n 3 - Delete Recipe\n 4 - View {username}'s Recipes\n 5 - Logout")
        choice = input("Your choice: ").strip()
        if choice == "1":
            user_recipes.add_recipe()
        elif choice == "2":
            user_recipes.edit_recipe()
        elif choice == "3":
            user_recipes.delete_recipe()
        elif choice == "4":
            user_recipes.print_recipes()
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid option, please try again.")

def main():
    main_menu()
    print("Thank you for using your Recipe Book!")
    print(f.renderText("Goodbye!"))

# Call main
if __name__ == "__main__":
    main()

    






