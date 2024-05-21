from flask import current_app
from flask_mysqldb import MySQLdb
from flask_login import UserMixin
from app import bcrypt
from app import mysql

class Usuario(UserMixin):
    def __init__(self, id, nome_usuario, senha):
        self.id = id
        self.nome_usuario = nome_usuario
        self.senha = senha

    @staticmethod
    def get_by_email(email):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM usuarios WHERE nome_usuario = %s", (email,))
        user_data = cursor.fetchone()
        cursor.close()
        if user_data:
            return Usuario(user_data['id'], user_data['nome_usuario'], user_data['senha'])
        return None

    def verificar_senha(self, senha):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM usuarios WHERE senha = %s", (senha,))
        user_data = cursor.fetchone()
        cursor.close()
        if user_data:
            return Usuario(user_data['id'], user_data['nome_usuario'], user_data['senha'])
        return None
       # return bcrypt.check_password_hash(self.senha, senha)

