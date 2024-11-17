import tkinter as tk
from tkinter import messagebox
import csv
import os

# File to store user data
USER_DATA_FILE = "users.csv"

# Function to initialize CSV file
def initialize_csv():
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])  # Header for CSV

# Function to verify credentials
def verify_credentials(username, password):
    initialize_csv()
    with open(USER_DATA_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username and row["password"] == password:
                return True
    return False

# Function to register a new user
def register_user(username, password):
    initialize_csv()
    with open(USER_DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

# Login Window
def login_window(parent):
    login_win = tk.Toplevel(parent)
    login_win.title("Login")
    login_win.geometry("800x550")

    # Create frames for two sections
    left_frame = tk.Frame(login_win, width=400, height=600)
    left_frame.pack(side="left", fill="both", expand=True)

    right_frame = tk.Frame(login_win, width=400, height=600)
    right_frame.pack(side="right", fill="both", expand=True)

    # Load and resize image in the left frame
    cover_image = tk.PhotoImage(file="assets/fonfo.png").subsample(2, 2)  # Adjust the subsample value as needed
    cover_label = tk.Label(left_frame, image=cover_image)
    cover_label.image = cover_image  # Keep a reference to avoid garbage collection
    cover_label.pack(fill="both", expand=True)

    # Centering widgets in the right frame using grid
    right_frame.grid_columnconfigure(0, weight=1)  # Center align items in the grid

    # Username field in the right frame
    tk.Label(right_frame, text="Username:").grid(row=0, column=0, pady=(20, 5))
    username_entry = tk.Entry(right_frame)
    username_entry.grid(row=1, column=0, pady=5)

    # Password field
    tk.Label(right_frame, text="Password:").grid(row=2, column=0, pady=(10, 5))
    password_entry = tk.Entry(right_frame, show="*")
    password_entry.grid(row=3, column=0, pady=5)

    # Function to handle login
    def handle_login():
        username = username_entry.get()
        password = password_entry.get()
        if verify_credentials(username, password):
            messagebox.showinfo("Login Successful", "Welcome!")
            login_win.destroy()  # Close login window if successful
            parent.deiconify()   # Show the main application window
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    # Function to handle registration
    def handle_register():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            register_user(username, password)
            messagebox.showinfo("Registration Successful", "You can now log in!")
        else:
            messagebox.showerror("Error", "Please enter both username and password")

    # Load button images from assets folder
    login_button_image = tk.PhotoImage(file="assets/log.png")
    register_button_image = tk.PhotoImage(file="assets/reg.png")

    # Login and Register buttons with respective images
    login_button = tk.Button(right_frame, image=login_button_image, command=handle_login)
    login_button.grid(row=4, column=0, pady=(20, 5))

    register_button = tk.Button(right_frame, image=register_button_image, command=handle_register)
    register_button.grid(row=5, column=0, pady=5)

    # Keep references to the images to prevent them from being garbage collected
    login_win.login_button_image = login_button_image
    login_win.register_button_image = register_button_image

    # Hide main app window until login
    parent.withdraw()