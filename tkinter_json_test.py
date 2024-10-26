import tkinter as tk
from tkinter import messagebox, Toplevel, StringVar, OptionMenu
import csv
import os

data_file = 'users.csv'

class Recipe:
    def __init__(self, meal_category, dish_name, ingredients, cooking_directions):
        self.meal_category = meal_category
        self.dish_name = dish_name
        self.ingredients = ingredients
        self.cooking_directions = cooking_directions

    def save_to_csv(self, user_file):
        # Save the recipe data to the user's CSV file
        with open(user_file, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([self.meal_category, self.dish_name, self.ingredients, self.cooking_directions])

    # @staticmethod
    def load_from_csv(user_file):
        recipes = []
        if os.path.exists(user_file):
            with open(user_file, mode='r', newline='') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                for row in reader:
                    if len(row) == 4:
                        recipes.append(Recipe(*row))
        return recipes

def load_users():
    users = {}
    if os.path.exists(data_file):
        with open(data_file, mode='r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    username, password = row
                    users[username] = password
    return users

def save_user(username, password):
    with open(data_file, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username, password])

    # Create a blank CSV file for storing recipes for this user
    user_recipe_file = f"{username}.csv"
    with open(user_recipe_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Meal Category", "Dish Name", "Ingredients", "Cooking Directions"])  # CSV header

users_data = load_users()

def register_user():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in users_data:
        messagebox.showerror("Error", "User already exists!")
    else:
        save_user(username, password)
        users_data[username] = password
        messagebox.showinfo("Success", "User registered successfully!")
        clear_fields()

def login_user():
    username = username_entry.get()
    password = password_entry.get()

    if username in users_data and users_data[username] == password:
        messagebox.showinfo(f"Login successful!", f"{username} Recipes!")
        open_main_window(username)
        root.withdraw()
    else:
        messagebox.showerror("Error", "Invalid username or password!")
        clear_fields()

def clear_fields():
    password_entry.delete(0, tk.END)


def open_main_window(username):
    main_window = Toplevel(root)
    main_window.title("Recipe Manager")
    user_file = f"{username}.csv"

    # Load recipes for this user
    recipe_options = Recipe.load_from_csv(user_file)

    # Dropdown menu for recipes, showing dish names
    recipe_var = StringVar(main_window)
    if recipe_options:
        recipe_var.set(recipe_options[0].dish_name)  # Set the first recipe as default
    else:
        recipe_var.set("No recipes available")  # Default message if no recipes
    
    # Check for no recipes and use a default option if necessary
    dropdown_options = [recipe.dish_name for recipe in recipe_options] or ["No recipes available"]
    dropdown = OptionMenu(main_window, recipe_var, *dropdown_options)
    dropdown.grid(row=0, column=0, padx=10, pady=10)

    add_button = tk.Button(main_window, text="Add New Recipe", command=lambda: add_recipe(user_file))
    edit_button = tk.Button(main_window, text="Edit Recipe", command=lambda: edit_recipe(user_file, recipe_var.get()))
    delete_button = tk.Button(main_window, text="Delete Recipe", command=lambda: delete_recipe(user_file, recipe_var.get()))

    add_button.grid(row=0, column=1, padx=10, pady=10)
    edit_button.grid(row=1, column=1, padx=10, pady=10)
    delete_button.grid(row=2, column=1, padx=10, pady=10)



def add_recipe(user_file):
    # Temporary: Add a sample recipe for demonstration
    new_recipe = Recipe("Dinner", "Sample Dish", "Tomatoes, Pasta", "Cook pasta, add sauce")
    new_recipe.save_to_csv(user_file)
    print(f"Added {new_recipe.dish_name} to {user_file}")

def edit_recipe(user_file, dish_name):
    print(f"Editing recipe {dish_name} in {user_file}")

def delete_recipe(user_file, dish_name):
    print(f"Deleting recipe {dish_name} from {user_file}")

# Create the main window
root = tk.Tk()
root.title("User Login")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Login", command=login_user).grid(row=1, column=2, padx=10, pady=10)
tk.Button(root, text="Register", command=register_user).grid(row=2, column=0, padx=0, pady=10)

root.mainloop()
