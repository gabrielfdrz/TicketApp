import mysql.connector

def connect_to_database():
    try:
        # Configurações para conectar ao seu banco de dados MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Athon123",
            database="ticket_db"
        )
        print("Conexão bem-sucedida!")
        return connection
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
