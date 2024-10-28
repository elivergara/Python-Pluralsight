###############################################################
# CS50P: Introduction to Programming with Python
# Harvard University
# Final Project: Digital Recipe Book
# Author: Eli Vergara
# Date: October 28-2024
#
# Description:
# This program is a digital recipe book that allows multiple users to create, store, edit, and print recipes. 
# It includes features such as:
#   - User authentication to enable personalized recipe storage.
#   - The ability to create, read, update, and delete individual recipes.
#   - The ability to print copies of any saved recipe.
#
# Purpose:
# This was a request from my wife as she wants to have a way to toganize and retrieve her recipes.
#
# Requirements:
# Python 3 or above (this was made using 3.12)
# Additional libraries: [csv, os, sys], in the future tkinter as I continue to learn how to use it.
################################################################
import csv
import sys

def main_menu(num: int = 0) -> int:
    """ Gives user a choice to 1) add a new user, or 2) enter the program"""
    if num == 1:
        create_user()
    elif num == 2:
        print("Loading...")
    else:
        sys.exit("You must enter 1 or 2")

def create_user():
    """creates new username and password, and creates a recipes file for the newly registered user """
    register_user = input("Enter a username: ").lower().strip()
    register_pwd = input(f"Enter a password for {register_user}: ").strip()

    with open("users.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["user", "password"])
        writer.writerow({"user": register_user, "password": register_pwd})

    user_recipe_file = f"{register_user}.csv"
    with open(user_recipe_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Meal Category", "Dish Name", "Ingredients", "Cooking Directions"])


def main():
    try:
        num = int(input("Select from the following options:\n 1 to register a new user \n 2 to enter the program "))
        main_menu(num)
    except ValueError:
        sys.exit("You must enter 1 or 2")

# Call main
if __name__ == "__main__":
    main()

    






