import streamlit as st
from db import get_pets_by_owner

def view_data(owner_username):
    st.title("Dados do Pet")
    
    pets = get_pets_by_owner(owner_username)
    if not pets:
        st.write("Nenhum pet encontrado.")
        return
    
    pet_names = [pet[1] for pet in pets]  # Posição do nome do pet
    selected_pet_name = st.selectbox("Selecione o Pet", pet_names)

    selected_pet_data = next((pet for pet in pets if pet[1] == selected_pet_name), None)
    if selected_pet_data:
        st.write(f"Nome: {selected_pet_data[1]}")
        st.write(f"Tipo: {selected_pet_data[2]}")
        st.write(f"Raça: {selected_pet_data[3]}")
        st.write(f"Gênero: {selected_pet_data[4]}")
        st.write(f"Peso: {selected_pet_data[5]} kg")
        st.write(f"Altura: {selected_pet_data[6]} cm")
        
        # Calculando IMC
        weight = selected_pet_data[5]
        height = selected_pet_data[6]
        if weight > 0 and height > 0:
            bmi = weight / (height ** 2)
            st.write(f"IMC: {bmi:.2f} kg/m²")
        else:
            st.warning("Peso ou altura não estão definidos para calcular o IMC.")
        
        st.write(f"Batimentos Cardíacos: {selected_pet_data[7]} bpm")
        st.write(f"Passos por Dia: {selected_pet_data[8]}")
        st.write(f"Consumo de Água por Dia: {selected_pet_data[9]:.2f} L")
        st.write(f"Consumo de Comida por Dia: {selected_pet_data[10]:.2f} g")
        st.write(f"Pressão: {selected_pet_data[11]} mmHg")
    else:
        st.error("Pet não encontrado.")

