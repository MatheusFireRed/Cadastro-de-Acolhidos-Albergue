import sqlite3


def conectarDB():

    nome_db = "acolhimento.db"

    conexao = sqlite3.connect(nome_db)

    cursor = conexao.cursor()

    return conexao, cursor

