# controllers/auth_controller.py
from db_model import create_user, get_user
import re

def handle_create_account(username, email, password):
    if not username or not email or not password:
        return "Todos os campos são obrigatórios."

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Formato de e-mail inválido. Por favor, insira um e-mail válido."

    if get_user(username):
        return "Nome de usuário já existe! Por favor, escolha outro."

    create_user(username, email, password)
    return "Conta criada com sucesso!"

def handle_login(username, password):
    if not username or not password:
        return "Nome de usuário e senha são obrigatórios."

    user = get_user(username)
    if user:
        stored_password = user[2]
        if password == stored_password:
            return f"Bem-vindo, {username}!"
        else:
            return "Senha incorreta."
    else:
        return "Usuário não encontrado."