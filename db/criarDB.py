import sqlite3
import os
from db import conexaoDB
from functions.log import log

nome_db = "acolhimento.db"
base_dir = os.path.dirname(os.path.dirname(__file__))
caminho_db = os.path.join(base_dir, nome_db)


def criarDB():

    log("Verificando banco de dados...")

    conexao, cursor = conexaoDB.conectarDB()

    try:

        # Tabela ACOLHIDOS
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS acolhidos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT UNIQUE NOT NULL,
                nome_mae TEXT,
                data_nasc TEXT
            )
        """)

        log("Tabela acolhidos verificada/criada.")

        # Tabela RETORNOS
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS retornos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_acolhido INTEGER NOT NULL,
                data_retorno TEXT NOT NULL,
                FOREIGN KEY (id_acolhido) REFERENCES acolhidos(id)
            )
        """)

        log("Tabela retornos verificada/criada.")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS observacoes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_acolhido INTEGER NOT NULL,
                observacao TEXT NOT NULL,
                FOREIGN KEY (id_acolhido) REFERENCES acolhidos(id)
            )
        """)

        log("Tabela observacoes verificada/criada.")

        conexao.commit()

    except Exception as e:
        log(f"Erro ao criar banco: {e}")

    finally:
        cursor.close()
        conexao.close()