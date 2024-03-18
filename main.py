from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Rota para criar o banco de dados e tabela
@app.route('/criar_banco')
def criar_banco():
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tickets 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 titulo TEXT, descricao TEXT)''')
    conn.commit()
    conn.close()
    return 'Banco de dados criado com sucesso!'

# Lista de tickets (simulando o banco de dados)
# Removido pois agora os dados serão armazenados no SQLite

@app.route('/')
def home():
    return render_template('home.html')

# Rota para o formulário de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Aqui você lida com os dados do formulário de login
        # Por exemplo, autentica o usuário e redireciona para outra página
        return redirect(url_for('abrir_ticket'))
    else:
        return render_template('login.html')

# Rota para abrir um ticket
@app.route('/abrir_ticket', methods=['GET', 'POST'])
def abrir_ticket():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        conn = sqlite3.connect('tickets.db')
        c = conn.cursor()
        c.execute('INSERT INTO tickets (titulo, descricao) VALUES (?, ?)', (titulo, descricao))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template('abrir_ticket.html')

# Rota para visualizar todos os tickets
@app.route('/tickets')
def listar_tickets():
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tickets')
    tickets = c.fetchall()
    conn.close()
    return render_template('listar_tickets.html', tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True)
