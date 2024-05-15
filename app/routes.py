from flask import render_template, redirect, url_for, flash, request
from app import app, db, bcrypt
from app.forms.login_usuario import LoginForm
from app.models.usuarios import Usuario
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(nome_usuario=form.nome_usuario.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form.senha.data):
            login_user(usuario)
            flash('Você está logado!', 'success')
            return redirect(url_for('acompanhamentos'))
        else:
            flash('Login falhou. Verifique nome de usuário e senha.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/acompanhamentos")
@login_required
def acompanhamentos():
    return render_template('acompanhamentos.html', title='Acompanhamentos')

@app.route('/ticket_aberto')
def ticket_aberto():
    return render_template('ticket_aberto.html')

@app.route('/ticket_encerrado')
def ticket_encerrado():
    return render_template('ticket_encerrado.html')
