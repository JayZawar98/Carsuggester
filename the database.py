#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Create a SQLite database and cursor
import sqlite3

# Create a SQLite database and cursor
conn = sqlite3.connect("Databasexx.db")
cursor = conn.cursor()

# Create the 'gaadya' table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS gaadya (id INTEGER PRIMARY KEY, name TEXT, price TEXT, combustion_type TEXT, model TEXT, transmission TEXT, color TEXT, variant TEXT)")

sample_data = [
    (1, "Honda City", "10 lacs", "Diesel", "Sedan", "Manual", "Black", "Base"),
    (2, "Honda City", "10 lacs", "Diesel", "Sedan", "Manual", "White", "Base"),
    (3, "Honda City", "10 lacs", "Petrol", "Sedan", "Automatic", "Black", "Top"),
    (4, "Honda City", "10 lacs", "Petrol", "Sedan", "Automatic", "White", "Top"),
    (5, "Tata Harrier", "5 lacs", "Diesel", "SUV", "Manual", "White", "Base"),
    (6, "Tata Harrier", "5 lacs", "Diesel", "SUV", "Manual", "Black", "Base"),
    (7, "Tata Harrier", "5 lacs", "Petrol", "SUV", "Automatic", "White", "Top"),
    (8, "Tata Harrier", "5 lacs", "Petrol", "SUV", "Automatic", "Black", "Top"),
    (9, "Hyundai Verna", "5 lacs", "Petrol", "Sedan", "Manual", "Black", "Base"),
    (10, "Hyundai Verna", "5 lacs", "Petrol", "Sedan", "Manual", "White", "Base"),
    (11, "Hyundai Verna", "5 lacs", "Diesel", "Sedan", "Automatic", "Black", "Top"),
    (12, "Hyundai Verna", "5 lacs", "Diesel", "Sedan", "Automatic", "White", "Top"),
    (13, "Toyota Fortuner", "10 lacs", "Petrol", "SUV", "Manual", "Black", "Base"),
    (14, "Toyota Fortuner", "10 lacs", "Petrol", "SUV", "Manual", "White", "Base"),
    (15, "Toyota Fortuner", "10 lacs", "Diesel", "SUV", "Automatic", "Black", "Top"),
    (16, "Toyota Fortuner", "10 lacs", "Diesel", "SUV", "Automatic", "White", "Top"),
    (17, "Mahindra XUV 700", "10 lacs", "Petrol", "SUV", "Manual", "Black", "Base"),
    (18, "Mahindra XUV 700", "10 lacs", "Petrol", "SUV", "Manual", "White", "Base"),
    (19, "Mahindra XUV 700", "10 lacs", "Diesel", "SUV", "Automatic", "Black", "Top"),
    (20, "Mahindra XUV 700", "10 lacs", "Diesel", "SUV", "Automatic", "White", "Top"),
    (21, "Skoda Slavia", "10 lacs", "Petrol", "Sedan", "Manual", "Black", "Base"),
    (22, "Skoda Slavia", "10 lacs", "Petrol", "Sedan", "Manual", "White", "Base"),
    (23, "Skoda Slavia", "10 lacs", "Diesel", "Sedan", "Automatic", "Black", "Top"),
    (24, "Skoda Slavia", "10 lacs", "Diesel", "Sedan", "Automatic", "White", "Top"),
    (25, "Tata Tigor", "5 lacs", "Petrol", "Sedan", "Manual", "White", "Base"),
    (26, "Tata Tigor", "5 lacs", "Petrol", "Sedan", "Manual", "Black", "Base"),
    (27, "Tata Tigor", "5 lacs", "Diesel", "Sedan", "Automatic", "White", "Top"),
    (28, "Tata Tigor", "5 lacs", "Diesel", "Sedan", "Automatic", "Black", "Top"),
    (29, "Mahindra Thar", "10 lacs", "Petrol", "SUV", "Manual", "White", "Base"),
    (30, "Mahindra Thar", "10 lacs", "Petrol", "SUV", "Manual", "Black", "Base"),
    (31, "Mahindra Thar", "10 lacs", "Diesel", "SUV", "Automatic", "White", "Top"),
    (32, "Mahindra Thar", "10 lacs", "Diesel", "SUV", "Automatic", "Black", "Top"),
    (33, "Maruti Dzire", "5 lacs", "Petrol", "Sedan", "Manual", "White", "Base"),
    (34, "Maruti Dzire", "5 lacs", "Petrol", "Sedan", "Manual", "Black", "Base"),
    (35, "Maruti Dzire", "5 lacs", "Diesel", "Sedan", "Automatic", "White", "Top"),
    (36, "Maruti Dzire", "5 lacs", "Diesel", "Sedan", "Automatic", "Black", "Top"),
    (37, "Hyundai Creta", "5 lacs", "Petrol", "SUV", "Manual", "White", "Base"),
    (38, "Hyundai Creta", "5 lacs", "Petrol", "SUV", "Manual", "Black", "Base"),
    (39, "Hyundai Creta", "5 lacs", "Diesel", "SUV", "Automatic", "White", "Top"),
    (40, "Hyundai Creta", "5 lacs", "Diesel", "SUV", "Automatic", "Black", "Top"),
]

 
cursor.executemany("INSERT INTO gaadya (id, name, price, combustion_type, model, transmission, color, variant)  VALUES (?, ?, ?, ?, ?, ?, ?, ?)", sample_data)

conn.commit()
conn.close()

