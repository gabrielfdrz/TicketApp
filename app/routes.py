from flask import render_template, redirect, url_for, request, flash, current_app
from flask_login import login_user, logout_user, login_required
from app import app, mysql
from app.models.usuarios import Usuario
from app.models.registrar_ticket import Ticket
from app.models.ticket_status import TicketStatus
from app.forms.registrar_ticket import TicketForm
from app.forms.ticket_status import TicketStatusForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TicketForm()
    if form.validate_on_submit():
        tipo = form.DS_TIPO.data
        usuario = form.NM_USUARIO.data
        matricula = form.CD_MATRICULA.data
        area = form.DS_AREA.data
        posto = form.DS_POSTO.data
        origem = form.DS_ORIGEM.data
        classificacao = form.DS_CLASSIFICACAO.data
        problema = form.DS_PROBLEMA.data
        acao = form.DS_ACAO.data
        solucao = form.DS_SOLUCAO.data
        responsavel = form.NM_RESPONSAVEL.data

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO TICKET (DS_TIPO, NM_USUARIO, CD_MATRICULA, DS_AREA, DS_POSTO, DS_ORIGEM, DS_CLASSIFICACAO, DS_PROBLEMA, DS_ACAO, DS_SOLUCAO, NM_RESPOSAVEL) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (tipo, usuario, matricula, area, posto, origem, classificacao, problema, acao, solucao, responsavel))
        mysql.connection.commit()
        cursor.close()

        flash('Ticket criado com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


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

@app.route('/acompanhamento', methods=['GET', 'POST'])
@login_required
def acompanhamento():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM TICKET")
    tickets = cursor.fetchall()
    cursor.close()
    return render_template('acompanhamento.html', tickets=tickets)

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
