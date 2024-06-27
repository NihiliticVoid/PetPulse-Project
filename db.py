import sqlite3

def init_db():
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()

    # Criação da tabela users (se não existir)
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, email TEXT, password TEXT)''')

    # Criação da tabela pets (se não existir)
    c.execute('''CREATE TABLE IF NOT EXISTS pets
                 (owner_username TEXT, pet_name TEXT, pet_type TEXT, breed TEXT, gender TEXT,
                  weight REAL, height REAL,
                  heart_rate INTEGER, steps INTEGER, water_consumption INTEGER,
                  food_consumption INTEGER, pressure INTEGER,
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
    c.execute("INSERT INTO pets (owner_username, pet_name, pet_type, breed, gender, weight, height) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (owner_username, pet_name, pet_type, breed, gender, 0.0, 0.0))  # Inicializando peso e altura com 0.0
    conn.commit()
    conn.close()

def get_pets_by_owner(owner_username):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute("SELECT * FROM pets WHERE owner_username=?", (owner_username,))
    pets = c.fetchall()
    conn.close()
    return pets

def add_pet_data(owner_username, pet_name, heart_rate, steps, water_consumption, food_consumption, pressure, weight, height):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute("UPDATE pets SET heart_rate=?, steps=?, water_consumption=?, food_consumption=?, pressure=?, weight=?, height=? WHERE owner_username=? AND pet_name=?",
              (heart_rate, steps, water_consumption, food_consumption, pressure, weight, height, owner_username, pet_name))
    conn.commit()
    conn.close()

def delete_pet(owner_username, pet_name):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute("DELETE FROM pets WHERE owner_username=? AND pet_name=?", (owner_username, pet_name))
    conn.commit()
    conn.close()