#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox
import sqlite3

def submit_registration():
    # Registration logic here
    username = entrya.get()
    mobile_number = entryb.get()
    email = entry3.get()
    password = entry4.get()

    # Add your validation logic here
    if not (username or mobile_number or email or password):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Check if username is unique
    connection = sqlite3.connect("malik.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()
    
    print(existing_user)
    if existing_user:
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        return

    # If username is unique, proceed with insertion
    
    cursor.execute("INSERT INTO users (username, mobile_number, email, password) VALUES (?, ?, ?, ?)", (username, mobile_number, email, password))
    connection.commit()
    connection.close()

    messagebox.showinfo("Success", "Account created successfully!")
    show_login_frame()

def login():
    # Login logic here
    username = entry1.get()
    password = entry2.get()

    if not (username and password):
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    connection = sqlite3.connect("malik.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    connection.close()

    if user:
        messagebox.showinfo("Success", "Login successful!")
        login_frame.pack_forget()
        registration_frame.pack_forget()
        car_selection_frame.pack()
        print("Login successful")
        # Add code to proceed after successful login
    else:
        messagebox.showerror("Error", "Invalid username or password.")

def display_car():
    # Car selection logic here
    price = price_var.get()
    combustion = combustion_var.get()
    model = model_var.get()
    transmission = transmission_var.get()
    color = color_var.get()
    variant = variant_var.get()

    conn = sqlite3.connect("Databasexx.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM gaadya WHERE price = ? AND combustion_type = ? AND model = ? AND transmission = ? AND color = ? AND  variant = ? ",(price, combustion, model, transmission, color, variant))
    result = cursor.fetchone()
    conn.close()

    if result:
        suitable_car_label.config(text="Suitable Car:" + result[0], font=("Arial", 16))
    else:
        suitable_car_label.config(text="No suitable car found.", font=("Arial", 16))

window = tk.Tk()
window.title("Car Selection App")
window.geometry('720x720')

# Create frames for registration, login, and car selection
registration_frame = tk.Frame(window)
login_frame = tk.Frame(window)
car_selection_frame = tk.Frame(window)

def show_registration_frame():
    registration_frame.pack()
    login_frame.pack_forget()
    car_selection_frame.pack_forget()

def show_login_frame():
    login_frame.pack()
    registration_frame.pack_forget()
    car_selection_frame.pack_forget()

def show_car_selection_frame():
    registration_frame.pack_forget()
    registration_button.pack_forget()
    login_frame.pack_forget()
    car_selection_frame.pack()

# Registration frame
label1 = tk.Label(registration_frame, text="Register for a new account!!", font=("Helvetica", 24))
label1.pack(pady=10)

label2 = tk.Label(registration_frame, text="Username", font=("Helvetica", 14))
label2.pack()
entrya = tk.Entry(registration_frame, width=50, font=("Helvetica", 12), borderwidth=10, justify='center')
entrya.pack(pady=10)

label3 = tk.Label(registration_frame, text="Mobile number", font=("Helvetica", 14))
label3.pack()
entryb = tk.Entry(registration_frame, width=50, font=("Helvetica", 12), borderwidth=10, justify='center')
entryb.pack(pady=10)

label4 = tk.Label(registration_frame, text="Email id", font=("Helvetica", 14))
label4.pack()
entry3 = tk.Entry(registration_frame, width=50, font=("Helvetica", 12), borderwidth=10, justify='center')
entry3.pack(pady=10)

label5 = tk.Label(registration_frame, text="Password", font=("Helvetica", 14))
label5.pack()
entry4 = tk.Entry(registration_frame, width=50, font=("Helvetica", 12), borderwidth=10, justify='center', show='*')
entry4.pack(pady=10)

submit_registration_button = tk.Button(registration_frame, command=submit_registration, text="Register", font=("Helvetica", 14), bg="red", fg="white")
submit_registration_button.pack(pady=10)

# Login frame
label2 = tk.Label(login_frame, text="Welcome to Login", font=("Helvetica", 14))
label2.pack()

label2 = tk.Label(login_frame, text="Username", font=("Helvetica", 14))
label2.pack()
entry1 = tk.Entry(login_frame, width=50, font=("Helvetica", 12), borderwidth=10, justify='center')
entry1.pack(pady=10)

label3 = tk.Label(login_frame, text="Password", font=("Helvetica", 14))
label3.pack()
entry2 = tk.Entry(login_frame, width=50, font=("Helvetica", 12), borderwidth=10, justify='center', show='*')
entry2.pack(pady=10)

login_button = tk.Button(login_frame, command=login, text="Login", font=("Helvetica", 14))
login_button.pack()

# Car Selection frame
price_var = tk.StringVar()
price_label = tk.Label(car_selection_frame, text="Select Price:", font=("Arial", 14))
price_label.pack()
price_dropdown = tk.OptionMenu(car_selection_frame, price_var, "5 lacs", "10 lacs")
price_dropdown.pack()

combustion_var = tk.StringVar()
combustion_label = tk.Label(car_selection_frame, text="Select Combustion Type:", font=("Arial", 14))
combustion_label.pack()
combustion_dropdown = tk.OptionMenu(car_selection_frame, combustion_var, "Petrol", "Diesel")
combustion_dropdown.pack()

model_var = tk.StringVar()
model_label = tk.Label(car_selection_frame, text="Select Model:", font=("Arial", 14))
model_label.pack()
model_dropdown = tk.OptionMenu(car_selection_frame, model_var, "Sedan", "SUV")
model_dropdown.pack()

transmission_var = tk.StringVar()
transmission_label = tk.Label(car_selection_frame, text="Select Transmission:", font=("Arial", 14))
transmission_label.pack()
transmission_dropdown = tk.OptionMenu(car_selection_frame, transmission_var, "Automatic", "Manual")
transmission_dropdown.pack()

color_var = tk.StringVar()
color_label = tk.Label(car_selection_frame, text="Select Color:", font=("Arial", 14))
color_label.pack()
color_dropdown = tk.OptionMenu(car_selection_frame, color_var, "Black", "White")
color_dropdown.pack()

variant_var = tk.StringVar()
variant_label = tk.Label(car_selection_frame, text="Select Variant:", font=("Arial", 14))
variant_label.pack()
variant_dropdown = tk.OptionMenu(car_selection_frame, variant_var, "Top", "Base")
variant_dropdown.pack()

submit_car_button = tk.Button(car_selection_frame, text="Submit", command=display_car, font=("Arial", 16))
submit_car_button.pack()

suitable_car_label = tk.Label(car_selection_frame, text="", font=("Arial", 16))
suitable_car_label.pack()

# Set the initial view to the login frame
show_login_frame()

# Buttons to switch between frames
#login_button = tk.Button(window, text="Login", command=show_login_frame, font=("Helvetica", 14))
#login_button.pack(pady=10)


registration_button = tk.Button(login_frame, text="Register", command=show_registration_frame, font=("Helvetica", 14))
registration_button.pack(pady=10)

#car_selection_button = tk.Button(window, text="Car Selection", command=show_car_selection_frame, font=("Helvetica", 14))
#car_selection_button.pack(pady=10)

# Create a table for user accounts (if not already exists)
connection = sqlite3.connect("malik.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        mobile_number TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL, 
        password TEXT NOT NULL
    )
""")
connection.commit()
connection.close()

window.mainloop()


# In[ ]:




