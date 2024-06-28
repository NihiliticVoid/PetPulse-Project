# controllers/pet_controller.py
from db_model import add_pet, get_pets_by_owner, add_pet_data, delete_pet

def handle_add_pet(owner_username, pet_name, pet_type, breed, gender):
    if not pet_name or not pet_type or not breed or not gender:
        return "Por favor, preencha todos os campos."
    
    add_pet(owner_username, pet_name, pet_type, breed, gender)
    return "Pet adicionado com sucesso!"

def handle_add_pet_data(owner_username, selected_pet_name, heart_rate, steps, water_consumption, food_consumption, pressure, weight, height):
    if not selected_pet_name:
        return "Pet não encontrado."

    bmi = weight / (height * height) if height > 0 else 0.0
    add_pet_data(owner_username, selected_pet_name, heart_rate, steps, water_consumption, food_consumption, pressure, weight, height, bmi)
    return "Dados do pet atualizados com sucesso!"

def handle_delete_pet(owner_username, pet_name):
    delete_pet(owner_username, pet_name)
    return "Pet removido com sucesso!"