from flask import render_template, redirect, url_for, flash, request
from app import app, db, bcrypt
from app.forms.login_usuario import LoginForm
from app.models.usuarios import Usuario
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST': 
        email = request.form.get('UsuarioEmail')
        senha = request.form.get('UsuarioSenha')
        
        if email == 'admin@admin.com' and senha == 'admin123':
            return redirect(url_for('acompanhamento'))  # Nome da função, não do arquivo HTML

    return render_template('login.html')

@app.route('/acompanhamento')
def acompanhamento():
    return render_template('acompanhamento.html')

@app.route('/ticket_aberto')
def ticket_aberto():
    return render_template('ticket_aberto.html')

@app.route('/ticket_encerrado')
def ticket_encerrado():
    return render_template('ticket_encerrado.html')
