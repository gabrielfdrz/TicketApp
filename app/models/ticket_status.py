from app import mysql

class TicketStatus:
    def __init__(self, ticket_id, status):
        self.ticket_id = ticket_id
        self.status = status

    @staticmethod
    def create(ticket_id, status):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO TICKET_STATUS (CD_TICKET_ID, DS_STATUS) VALUES (%s, %s)", (ticket_id, status))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_last_status(ticket_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT DS_STATUS FROM TICKET_STATUS WHERE CD_TICKET_ID = %s ORDER BY CD_TICKET_STATUS_ID DESC LIMIT 1", (ticket_id,))
        last_status = cursor.fetchone()
        cursor.close()
        return last_status['DS_STATUS'] if last_status else 'N/A'
