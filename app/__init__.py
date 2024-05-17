from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
from flask_login import LoginManager
from config import Config 

app = Flask(__name__)

# Configurações do MySQL
app.config.from_object(Config)

# Inicialização do MySQL
mysql = MySQL(app)

# Inicialização do Bcrypt
bcrypt = Bcrypt()
bcrypt.init_app(app)

# Inicialização do LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes
from app.models.usuarios import Usuario
import MySQLdb

@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    cursor.close()
    if user_data:
        return Usuario(user_data['id'], user_data['email'], user_data['senha'])
    return None

