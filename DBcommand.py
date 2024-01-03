import sqlite3

class DataBase:
    #iniciando a classe e estabelecendo conexão
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
    
    #criar tabela caso não exista
    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS posto_de_molas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    systemCod TEXT NOT NULL,
                    name TEXT NOT NULL,
                    barcod TEXT NOT NULL
                )'''
        self.cursor.execute(sql)
        self.conn.commit()

    #inserir dados
    def insert(self, name, systemCod, barcod):
        valores = (systemCod, name, barcod)
        sql = '''INSERT INTO posto_de_molas
            (systemCod, name, barcod)
            values
            (?, ?, ?)'''
        self.cursor.execute(sql, valores)
        self.conn.commit()

    #selecionando todos os dados que tenham o system code desejado
    def selectSystemcodALL(self,systemCod):
        sql = '''SELECT * FROM posto_de_molas where systemCod == ?'''
        self.cursor.execute(sql, systemCod)

    #selecionando todos os codigos de barras
    def selectBarcodALL(self, barcod):
        sql = '''SELECT barcod FROM posto_de_molas'''
        self.cursor.execute(sql)

    def close(self):
        self.conn.close()