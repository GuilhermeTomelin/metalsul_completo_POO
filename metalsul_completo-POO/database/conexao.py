import os
import psycopg #postgresql
from dotenv import load_dotenv

load_dotenv()  #Carrega automaticamente as variáveis existentes no .env

class Conexao:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.database = os.getenv("DB_NAME") #OU DATABASE
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.conexao = psycopg.connect(
            host = self.host,
            port = self.port,
            dbname = self.database,
            user = self.user,
            password = self.password
        )
        self.cursor = self.conexao.cursor()
    
    def commit(self):
        self.conexao.commit()
    def rollback(self):
        self.conexao.rollback()
    def fechar(self):  #Fechar ou Close
        self.cursor.close()
        self.conexao.close()