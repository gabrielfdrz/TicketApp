from flask import current_app
from flask_mysqldb import MySQL
import MySQLdb.cursors

mysql = MySQL()

class Ticket:
    def __init__(self, cd_ticket_id=None, ds_tipo=None, nm_usuario=None, cd_matricula=None, ds_area=None, ds_posto=None, ds_origem=None, ds_classificacao=None, ds_problema=None, ds_acao=None, ds_solucao=None, nm_responsavel=None):
        self.cd_ticket_id = cd_ticket_id
        self.ds_tipo = ds_tipo
        self.nm_usuario = nm_usuario
        self.cd_matricula = cd_matricula
        self.ds_area = ds_area
        self.ds_posto = ds_posto
        self.ds_origem = ds_origem
        self.ds_classificacao = ds_classificacao
        self.ds_problema = ds_problema
        self.ds_acao = ds_acao
        self.ds_solucao = ds_solucao
        self.nm_responsavel = nm_responsavel

    @staticmethod
    def get_by_id(ticket_id):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM TICKET WHERE CD_TICKET_ID = %s', (ticket_id,))
        ticket_data = cursor.fetchone()
        cursor.close()
        if ticket_data:
            return Ticket(**ticket_data)
        return None

    @staticmethod
    def get_all():
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM TICKET')
        tickets = cursor.fetchall()
        cursor.close()
        return [Ticket(**ticket) for ticket in tickets]

    def save_to_db(self):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if self.cd_ticket_id:
            cursor.execute("""
                UPDATE TICKET SET
                    DS_TIPO = %s,
                    NM_USUARIO = %s,
                    CD_MATRICULA = %s,
                    DS_AREA = %s,
                    DS_POSTO = %s,
                    DS_ORIGEM = %s,
                    DS_CLASSIFICACAO = %s,
                    DS_PROBLEMA = %s,
                    DS_ACAO = %s,
                    DS_SOLUCAO = %s,
                    NM_RESPOSAVEL = %s
                WHERE CD_TICKET_ID = %s
            """, (
                self.ds_tipo, self.nm_usuario, self.cd_matricula, self.ds_area,
                self.ds_posto, self.ds_origem, self.ds_classificacao, self.ds_problema,
                self.ds_acao, self.ds_solucao, self.nm_responsavel, self.cd_ticket_id
            ))
        else:
            cursor.execute("""
                INSERT INTO TICKET (
                    DS_TIPO, NM_USUARIO, CD_MATRICULA, DS_AREA,
                    DS_POSTO, DS_ORIGEM, DS_CLASSIFICACAO, DS_PROBLEMA,
                    DS_ACAO, DS_SOLUCAO, NM_RESPOSAVEL
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                self.ds_tipo, self.nm_usuario, self.cd_matricula, self.ds_area,
                self.ds_posto, self.ds_origem, self.ds_classificacao, self.ds_problema,
                self.ds_acao, self.ds_solucao, self.nm_responsavel
            ))
            self.cd_ticket_id = cursor.lastrowid
        mysql.connection.commit()
        cursor.close()

    def delete_from_db(self):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM TICKET WHERE CD_TICKET_ID = %s', (self.cd_ticket_id,))
        mysql.connection.commit()
        cursor.close()
