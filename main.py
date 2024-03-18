from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def criar_banco():
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL,
                    tipo_de_usuario TEXT NOT NULL
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS tickets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    descricao TEXT NOT NULL,
                    status TEXT NOT NULL,
                    data_de_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    usuario_id INTEGER,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
                )''')
    conn.commit()
    conn.close()
criar_banco()

@app.route('/')
def home():
    return render_template('home.html')

# Rota para o formulário de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # formulário de login
        # autentica o usuário e redireciona para outra página
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
