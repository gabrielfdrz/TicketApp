from flask import render_template, redirect, url_for, request, flash, current_app
from flask_login import login_user, logout_user, login_required
from app import app, mysql
from app.models.usuarios import Usuario
from app.models.registrar_ticket import Ticket
from app.models.ticket_status import TicketStatus
from app.forms.registrar_ticket import TicketForm
from app.forms.ticket_status import TicketStatusForm

@app.route('/', methods=['GET', 'POST'])
def create_ticket():
    form = TicketForm()
    if form.validate_on_submit():
        cursor = mysql.connection.cursor() 
        cursor.execute("""
            INSERT INTO TICKET (DS_TIPO, NM_USUARIO, CD_MATRICULA, DS_AREA, DS_POSTO, DS_ORIGEM, DS_CLASSIFICACAO, DS_PROBLEMA, DS_ACAO, DS_SOLUCAO, NM_RESPOSAVEL) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            form.ds_tipo.data,
            form.nm_usuario.data,
            form.cd_matricula.data,
            form.ds_area.data,
            form.ds_posto.data,
            form.ds_origem.data,
            form.ds_classificacao.data,
            form.ds_problema.data,
            form.ds_acao.data,
            form.ds_solucao.data,
            form.nm_responsavel.data
        ))
        mysql.connection.commit()
        cursor.close()
        flash('Ticket criado com sucesso!', 'success')
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

@app.route('/acompanhamento', methods=['GET', 'POST'])
def acompanhamento():
    ticket_status_form = TicketStatusForm()

    if ticket_status_form.validate_on_submit():
        ticket_id = ticket_status_form.ticket_id.data
        novo_status = ticket_status_form.status.data

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM TICKET WHERE CD_TICKET_ID = %s", (ticket_id,))
        ticket = cursor.fetchone()

        if ticket:
            cursor.execute("INSERT INTO TICKET_STATUS (CD_TICKET_ID, DS_STATUS) VALUES (%s, %s)", (ticket_id, novo_status))
            mysql.connection.commit()
            flash(f'Status do ticket {ticket_id} atualizado para {novo_status}!', 'success')
        else:
            flash(f'Ticket com ID {ticket_id} não encontrado.', 'error')

        cursor.close()
        return redirect(url_for('acompanhamento'))

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM TICKET")
    tickets = cursor.fetchall()

    ticket_status_data = {}
    for ticket in tickets:
        cursor.execute("SELECT * FROM TICKET_STATUS WHERE CD_TICKET_ID = %s ORDER BY CD_TICKET_STATUS_ID DESC LIMIT 1", (ticket['CD_TICKET_ID'],))
        last_status = cursor.fetchone()
        ticket_status_data[ticket['CD_TICKET_ID']] = last_status['DS_STATUS'] if last_status else 'N/A'

    cursor.close()
    return render_template('acompanhamento.html', ticket_status_form=ticket_status_form, tickets=tickets, ticket_status_data=ticket_status_data)

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
