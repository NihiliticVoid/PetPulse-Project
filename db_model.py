# models/db.py
import sqlite3

def init_db():
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, email TEXT, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS pets
                 (owner_username TEXT, pet_name TEXT, pet_type TEXT, breed TEXT, gender TEXT,
                  heart_rate REAL DEFAULT 0.0, steps REAL DEFAULT 0.0, water_consumption REAL DEFAULT 0.0,
                  food_consumption REAL DEFAULT 0.0, pressure REAL DEFAULT 0.0,
                  weight REAL DEFAULT 0.0, height REAL DEFAULT 0.0, bmi REAL DEFAULT 0.0,
                  FOREIGN KEY(owner_username) REFERENCES users(username))''')
    conn.commit()
    conn.close()

def create_user(username, email, password):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    return user

def add_pet(owner_username, pet_name, pet_type, breed, gender):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute("INSERT INTO pets (owner_username, pet_name, pet_type, breed, gender) VALUES (?, ?, ?, ?, ?)",
              (owner_username, pet_name, pet_type, breed, gender))
    conn.commit()
    conn.close()

def get_pets_by_owner(owner_username):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute("SELECT * FROM pets WHERE owner_username=?", (owner_username,))
    pets = c.fetchall()
    conn.close()
    return pets

def add_pet_data(owner_username, pet_name, heart_rate, steps, water_consumption, food_consumption, pressure, weight, height, bmi):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute("UPDATE pets SET heart_rate=?, steps=?, water_consumption=?, food_consumption=?, pressure=?, weight=?, height=?, bmi=? WHERE owner_username=? AND pet_name=?",
              (heart_rate, steps, water_consumption, food_consumption, pressure, weight, height, bmi, owner_username, pet_name))
    conn.commit()
    conn.close()

def delete_pet(owner_username, pet_name):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute("DELETE FROM pets WHERE owner_username=? AND pet_name=?", (owner_username, pet_name))
    conn.commit()
    conn.close()