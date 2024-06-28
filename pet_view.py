# views/pet_view.py
import streamlit as st

def show_add_pet():
    st.title("Adicionar Pet")
    pet_name = st.text_input("Nome do Pet")
    pet_type = st.text_input("Tipo")
    breed = st.text_input("Raça")
    gender = st.selectbox("Gênero", ["Macho", "Fêmea"])
    return pet_name, pet_type, breed, gender, st.button("Salvar Pet")

def show_add_pet_data(pets):
    st.title("Adicionar Dados do Pet")
    pet_names = [pet[1] for pet in pets]
    selected_pet_name = st.selectbox("Selecione o Pet", pet_names)

    heart_rate = st.number_input("Batimentos Cardíacos", format="%.1f")
    steps = st.number_input("Quantidade de Passos", format="%.1f")
    water_consumption = st.number_input("Consumo de Água", format="%.1f")
    food_consumption = st.number_input("Consumo de Comida", format="%.1f")
    pressure = st.number_input("Medição de Pressão", format="%.1f")
    weight = st.number_input("Peso", format="%.1f")
    height = st.number_input("Altura", format="%.1f")

    return selected_pet_name, heart_rate, steps, water_consumption, food_consumption, pressure, weight, height, st.button("Salvar Dados")

def show_pet_data(pets):
    st.title("Dados do Pet")
    if not pets:
        st.write("Nenhum pet encontrado.")
        return None

    pet_names = [pet[1] for pet in pets]
    selected_pet_name = st.selectbox("Selecione o Pet", pet_names)

    selected_pet_data = next((pet for pet in pets if pet[1] == selected_pet_name), None)
    if selected_pet_data:
        st.write(f"Nome: {selected_pet_data[1]}")
        st.write(f"Tipo: {selected_pet_data[2]}")
        st.write(f"Raça: {selected_pet_data[3]}")
        st.write(f"Gênero: {selected_pet_data[4]}")
        st.write(f"Batimentos Cardíacos: {selected_pet_data[5]} bpm")
        st.write(f"Passos: {selected_pet_data[6]} passos/h")
        st.write(f"Consumo de Água: {selected_pet_data[7]} l/dia")
        st.write(f"Consumo de Comida: {selected_pet_data[8]} g/dia")
        st.write(f"Pressão: {selected_pet_data[9]} mmHg")
        st.write(f"Peso: {selected_pet_data[10]} kg")
        st.write(f"Altura: {selected_pet_data[11]} m")
        st.write(f"IMC: {selected_pet_data[12]} kg/m²")
    else:
        st.error("Pet não encontrado.")
    return selected_pet_name, st.button("Remover Pet")