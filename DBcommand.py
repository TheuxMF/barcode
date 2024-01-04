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
                    systemCod TEXT NOT NULL UNIQUE,
                    name TEXT NOT NULL,
                    barcod TEXT NOT NULL UNIQUE
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

    #retorna um nome de produto pelo codigo do sistema passado
    def selectName(self,systemCod):
        sql = '''SELECT name FROM posto_de_molas where systemCod=?'''
        self.cursor.execute(sql, (systemCod,))

        return self.cursor.fetchall()
    
    #retorna um barcode pelo codigo de sistema informado
    def selectBarcod(self,systemCod):      
        sql = '''SELECT barcod FROM posto_de_molas where systemCod=?'''
        self.cursor.execute(sql, (systemCod,))

        return self.cursor.fetchall()

    #retorna todos os systemCod do banco
    def selectSystemCodALL(self):
        sql = '''SELECT systemCod FROM posto_de_molas '''
        self.cursor.execute(sql)

        return self.cursor.fetchall()

    #retorna todos os codigos de barras no banco
    def selectBarcodALL(self):
        sql = '''SELECT barcod FROM posto_de_molas'''
        self.cursor.execute(sql)

        return self.cursor.fetchall()
        
    def close(self):
        self.conn.close()