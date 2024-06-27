import streamlit as st
from auth import create_account, login, logout
from pet_info import view_data
from pet_add import add_pet_info, add_pet_data_form
from db import init_db

# Defina a configuração da página
st.set_page_config(
    page_title="PetPulse",
    page_icon="PetPulse.ico"  # Altere para o caminho do seu ícone
)



def main():
    init_db()  # Inicializa o banco de dados

    # Adicione a imagem acima do título do menu
    st.sidebar.image("PetPulse.jpg", use_column_width=True)
    st.sidebar.title("Menu")

    st.get_option("theme.primaryColor")
    st.get_option("theme.textColor")


    if "username" not in st.session_state:
        choice = st.sidebar.radio("Navegação", ["Criar Conta", "Login"])
        if choice == "Criar Conta":
            create_account()
        elif choice == "Login":
            login()
    else:
        username = st.session_state["username"]
        st.sidebar.write(f"Bem-vindo, {username}!")

        choice = st.sidebar.radio("Navegação", ["Dados do Pet", "Adicionar Pet", "Adicionar Dados do Pet", "Sair"])
        if choice == "Dados do Pet":
            view_data(username)
        elif choice == "Adicionar Pet":
            add_pet_info(username)
        elif choice == "Adicionar Dados do Pet":
            add_pet_data_form(username)
        elif choice == "Sair":
            logout()

if __name__ == "__main__":
    main()