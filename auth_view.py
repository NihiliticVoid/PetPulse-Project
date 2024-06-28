# views/auth_view.py
import streamlit as st

def show_create_account():
    st.title("Criar Conta no PetPulse")
    username = st.text_input("Nome de Usuário", key="create_username")
    email = st.text_input("E-mail", key="create_email")
    password = st.text_input("Senha", type="password", key="create_password")
    return username, email, password, st.button("Cadastrar", key="register_button")

def show_login():
    st.title("Login no PetPulse")
    username = st.text_input("Nome de Usuário", key="login_username")
    password = st.text_input("Senha", type="password", key="login_password")
    return username, password, st.button("Entrar", key="login_button")

def show_logout(username):
    st.session_state.pop("username", None)
    st.rerun()  # Reinicia a aplicação