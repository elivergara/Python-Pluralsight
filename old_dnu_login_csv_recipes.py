import tkinter as tk
from tkinter import messagebox
import csv
import os

# Path to the user data file
DATA_FILE = 'users.csv'

def load_users():
    """Load users from a CSV file and return a dictionary of username: password."""
    users = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:  # Ensure each row has a username and password
                    username, password = row
                    users[username] = password
    return users

def save_user(username, password):
    """Append a new user to the CSV file."""
    with open(DATA_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username, password])

def register_user():
    """Handle user registration."""
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        messagebox.showerror("Error", "Username and password cannot be empty!")
        return

    if username in users_data:
        messagebox.showerror("Error", "User already exists!")
    else:
        save_user(username, password)
        users_data[username] = password  # Update in-memory data
        messagebox.showinfo("Success", "User registered successfully!")
        clear_fields()

def login_user():
    """Handle user login."""
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username in users_data and users_data[username] == password:
        messagebox.showinfo("Success", "Login successful!")
        root.destroy()  # Close the login window
    else:
        messagebox.showerror("Error", "Invalid username or password!")
        clear_fields()

def clear_fields():
    """Clear the password entry field."""
    password_entry.delete(0, tk.END)

# Load users into memory
users_data = load_users()

# Create the main window
root = tk.Tk()
root.title("User Login")

# Create and place the username and password labels and entries
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the buttons
tk.Button(root, text="Login", command=login_user).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Register", command=register_user).grid(row=2, column=0, padx=10, pady=10)
# Start the Tkinter main loop
root.mainloop()
