import sqlite3
import os
from db import conexaoDB
from functions.log import log

nome_db         = "acolhimento.db"
base_dir        = os.path.dirname(os.path.dirname(__file__))
caminho_debug   = os.path.join(base_dir, "debug.txt")
caminho_db      = os.path.join(base_dir, nome_db)


def criarDB():

    log("Virificando Banco de dados...")

    if not os.path.exists(caminho_db):
        print("Banco de dados não existe, criando...")

        log("Banco de dados não existente, criando...")

        conexao, cursor = conexaoDB.conectarDB()
  
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS acolhidos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT,
            nome_mae TEXT,
            data_nasc DATETIME
            )"""
        )

        conexao.commit()
        conexao.close()

        log("Banco de dados criado com sucesso!")
    else:
        print("Banco de dados já existe!")

        log("Banco de dados existente")



