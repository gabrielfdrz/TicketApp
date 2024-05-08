from flask import Flask, render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/acompanhamento')
def acompanhamentos():
    return render_template('acompanhamento.html')

@app.route('/ticket_aberto')
def ticket_aberto():
    return render_template('ticket_aberto.html')

@app.route('/ticket_encerrado')
def ticket_encerrado():
    return render_template('ticket_encerrado.html')
