import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key_facerecognition'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Athon123'
    MYSQL_DB = 'ticket_db'
    DEBUG = True
    
