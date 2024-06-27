import streamlit as st
from db import create_user, get_user

# Função para criar conta
def create_account():
    st.title("Criar Conta no Pet Pulse")
    username = st.text_input("Nome de Usuário", key="create_username")
    email = st.text_input("E-mail", key="create_email")
    password = st.text_input("Senha", type="password", key="create_password")

    if st.button("Cadastrar", key="register_button"):
        if not username or not email or not password:
            st.error("Todos os campos são obrigatórios.")
            return
        
        if get_user(username):
            st.error("Nome de usuário já existe! Por favor, escolha outro.")
        else:
            create_user(username, email, password)
            st.success("Conta criada com sucesso!")
            st.info("Agora você pode fazer login com seu nome de usuário e senha.")

# Função para login
def login():
    st.title("Login no Pet Pulse")

    with st.form(key='login_form'):
        username = st.text_input("Nome de Usuário", key="login_username")
        password = st.text_input("Senha", type="password", key="login_password")
        submit_button = st.form_submit_button(label='Entrar')

    if submit_button:
        if not username or not password:
            st.error("Nome de usuário e senha são obrigatórios.")
            return
        
        user = get_user(username)
        if user:
            stored_password = user[2]  # Considerando que a senha está na posição 2 da tupla
            if password == stored_password:
                st.session_state["username"] = username
                st.success(f"Bem-vindo, {username}!")
                st.experimental_rerun()
            else:
                st.error("Senha incorreta.")
        else:
            st.error("Usuário não encontrado.")

# Função para logout
def logout():
    if "username" in st.session_state:
        del st.session_state["username"]
        st.experimental_rerun()