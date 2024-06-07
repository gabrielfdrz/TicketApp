from flask import render_template, redirect, url_for, request, flash, current_app, make_response, send_file, jsonify
import pandas as pd
from flask_login import login_user, logout_user, login_required
from app import app, mysql
from app.models.usuarios import Usuario
from app.models.registrar_ticket import Ticket
from app.models.ticket_status import TicketStatus
from app.forms.registrar_ticket import TicketForm
from app.forms.ticket_status import TicketStatusForm
from app.forms.relatorio import Status
from datetime import datetime


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TicketForm()
    if form.validate_on_submit():
        tipo = form.tipo.data
        usuario = form.usuario.data
        matricula = form.matricula.data
        area = form.area.data
        posto = form.posto.data
        origem = form.origem.data
        classificacao = form.classificacao.data
        problema = form.problema.data
        acao = form.acao.data
        solucao = form.solucao.data
        responsavel = form.responsavel.data
        data_emissao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Captura a data e hora atuais

        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO TICKET (DS_TIPO, NM_USUARIO, CD_MATRICULA, DS_AREA, DS_POSTO, DS_ORIGEM, DS_CLASSIFICACAO, DS_PROBLEMA, DS_ACAO, DS_SOLUCAO, NM_RESPONSAVEL, DT_EMISSAO)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (tipo, usuario, matricula, area, posto, origem, classificacao, problema, acao, solucao, responsavel, data_emissao))
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

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/ticket/<int:ticket_id>')
def view_ticket(ticket_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM TICKET WHERE CD_TICKET_ID = %s", (ticket_id,))
    ticket = cursor.fetchone()
    cursor.close()
    if ticket:
        return render_template('ticket_aberto.html', ticket=ticket)
    else:
        flash('Ticket não encontrado.', 'danger')
        return redirect(url_for('index'))

@app.route('/encerrar_ticket/<int:ticket_id>', methods=['POST'])
def encerrar_ticket(ticket_id):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE TICKET
        SET DS_STATUS = 'ENCERRADO'
        WHERE CD_TICKET_ID = %s
    """, (ticket_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'success': True})

@app.route('/cancelar_ticket/<int:ticket_id>', methods=['POST'])
def cancelar_ticket(ticket_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM TICKET WHERE CD_TICKET_ID = %s", (ticket_id,))
    #cursor.execute("DELETE FROM TICKET_STATUS WHERE CD_TICKET_ID = %s", (ticket_id,))#
    mysql.connection.commit()
    cursor.close()
    flash('Ticket cancelado com sucesso!', 'success')
    return redirect(url_for('acompanhamento'))

@app.route('/acompanhamento')
def acompanhamento():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM TICKET")
    tickets = cursor.fetchall()
    cursor.close()
    return render_template('acompanhamento.html', tickets=tickets)

@app.route('/extrair_relatorio')
def extrair_relatorio():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM TICKET")
    tickets = cursor.fetchall()
    cursor.close()
    return render_template('extrair_relatorio.html', tickets=tickets)

