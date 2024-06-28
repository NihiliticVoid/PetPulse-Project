import streamlit as st
from db_model import init_db, get_pets_by_owner
from auth_view import show_create_account, show_login, show_logout
from pet_view import show_add_pet, show_add_pet_data, show_pet_data
from auth_controller import handle_create_account, handle_login
from pet_controller import handle_add_pet, handle_add_pet_data, handle_delete_pet

st.set_page_config(
    page_title="PetPulse",
    page_icon="PetPulse.ico"  
)

init_db()

def main():

    st.sidebar.image("PetPulse.jpg")  

    st.sidebar.title("Menu")
    if st.session_state.get("username"):  # Verifica se o usuário está logado
        username = st.session_state.get("username")
        
        st.sidebar.write(f"Bem-vindo, {username}!")
        
        menu_options = []

        # Verifica se há pets associados ao usuário
        pets = get_pets_by_owner(username)
        if pets:
            menu_options.extend(["Adicionar Pet", "Adicionar Dados do Pet", "Dados do Pet", "Logout"])
        else:
            menu_options.extend(["Adicionar Pet", "Logout"])

        menu = st.sidebar.radio("Navegação", menu_options)

        if menu == "Adicionar Pet":
            pet_name, pet_type, breed, gender, save_button = show_add_pet()
            if save_button:
                result = handle_add_pet(username, pet_name, pet_type, breed, gender)
                if "sucesso" in result:
                    st.success(result)
                    st.rerun()  # Força a atualização da página para mostrar as novas opções
                else:
                    st.error(result)

        elif menu == "Adicionar Dados do Pet":
            selected_pet_name, heart_rate, steps, water_consumption, food_consumption, pressure, weight, height, save_button = show_add_pet_data(pets)
            if save_button:
                result = handle_add_pet_data(username, selected_pet_name, heart_rate, steps, water_consumption, food_consumption, pressure, weight, height)
                st.success(result)

        elif menu == "Dados do Pet":
            selected_pet_name, delete_button = show_pet_data(pets)
            if delete_button:
                result = handle_delete_pet(username, selected_pet_name)
                st.success(result)

        elif menu == "Logout":
            show_logout(username)

    else:
        st.sidebar.subheader("Opções de Conta")
        menu = st.sidebar.radio("Navegação", ["Login", "Criar Conta"])

        if menu == "Login":
            username, password, login_button = show_login()
            if login_button:
                result = handle_login(username, password)
                if "Bem-vindo" in result:
                    st.success(result)
                    st.session_state.username = username
                    st.rerun()  # Força a atualização da página para mostrar o novo estado de login
                else:
                    st.error(result)

        elif menu == "Criar Conta":
            username, email, password, register_button = show_create_account()
            if register_button:
                result = handle_create_account(username, email, password)
                if "sucesso" in result:
                    st.success(result)
                else:
                    st.error(result)

if __name__ == "__main__":
    main()