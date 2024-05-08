from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
UPLOAD_FOLDER = './static/img'
ma = Marshmallow(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import routes
