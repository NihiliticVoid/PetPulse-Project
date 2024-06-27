import streamlit as st
from db import get_pets_by_owner, delete_pet

def delete_pet_info(owner_username):
    st.title("Remover Pet")

    pets = get_pets_by_owner(owner_username)
    if not pets:
        st.write("Nenhum pet encontrado.")
        return

    pet_names = [pet[1] for pet in pets]
    selected_pet_name = st.selectbox("Selecione o Pet para Remover", pet_names)

    if st.button("Remover Pet"):
        if selected_pet_name:
            delete_pet(owner_username, selected_pet_name)
            st.success(f"Pet '{selected_pet_name}' removido com sucesso!")
            st.experimental_rerun()
        else:
            st.error("Por favor, selecione um pet.")