from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Athon123@localhost/ticket_db'

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

from app.models.usuarios import Usuario
from app.routes import *

def criar_usuario_fixo():
    from app.models.usuarios import Usuario

    if not Usuario.query.filter_by(nome_usuario='admin@admin.com').first():
        hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
        novo_usuario = Usuario(nome_usuario='admin@admin.com', senha=hashed_password)
        db.session.add(novo_usuario)
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))




