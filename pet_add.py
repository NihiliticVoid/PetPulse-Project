import streamlit as st
from db import get_pets_by_owner, add_pet, add_pet_data

def add_pet_info(owner_username):
    st.title("Adicionar Pet")

    pet_name = st.text_input("Nome do Pet")
    pet_type = st.text_input("Tipo")
    breed = st.text_input("Raça")
    gender = st.selectbox("Gênero", ["Macho", "Fêmea"])

    if st.button("Salvar Pet"):
        if pet_name and pet_type and breed and gender:
            add_pet(owner_username, pet_name, pet_type, breed, gender)
            st.success("Pet adicionado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

def add_pet_data_form(owner_username):
    st.title("Adicionar Dados do Pet")

    pets = get_pets_by_owner(owner_username)
    if not pets:
        st.write("Nenhum pet encontrado.")
        return

    pet_names = [pet[1] for pet in pets]
    selected_pet_name = st.selectbox("Selecione o Pet", pet_names)

    heart_rate = st.number_input("Batimentos Cardíacos")
    steps = st.number_input("Quantidade de Passos (Diário)")
    water_consumption = st.number_input("Consumo de Água (Diário)")
    food_consumption = st.number_input("Consumo de Comida (Diário)")
    pressure = st.number_input("Medição de Pressão")
    weight = st.number_input("Peso (kg)")
    height = st.number_input("Altura (cm)")

    if st.button("Salvar Dados"):
        selected_pet_data = next((pet for pet in pets if pet[1] == selected_pet_name), None)
        if selected_pet_data:
            add_pet_data(owner_username, selected_pet_name, heart_rate, steps, water_consumption, food_consumption, pressure, weight, height)
            st.success("Dados do pet atualizados com sucesso!")
        else:
            st.error("Pet não encontrado.")