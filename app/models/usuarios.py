from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Usuario('{self.nome_usuario}')"


