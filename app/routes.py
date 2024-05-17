from flask import render_template, redirect, url_for, request, flash, current_app
from flask_login import login_user, logout_user, login_required
from app import app
from app.models.usuarios import Usuario

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST': 
        email = request.form.get('UsuarioEmail')
        senha = request.form.get('UsuarioSenha')
        
        usuario = Usuario.get_by_email(email)
        
        if usuario and usuario.verificar_senha(senha):
            login_user(usuario)
            return redirect(url_for('acompanhamento'))
        else:
            flash('Login ou senha incorretos. Por favor, tente novamente.', 'danger')
    
    return render_template('login.html')

@app.route('/acompanhamento')
@login_required
def acompanhamento():
    return render_template('acompanhamento.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/ticket_aberto')
def ticket_aberto():
    return render_template('ticket_aberto.html')

@app.route('/ticket_encerrado')
def ticket_encerrado():
    return render_template('ticket_encerrado.html')
