from db import conexaoDB
from functions.log import log


sql_insert = "INSERT INTO acolhidos (nome, cpf, nome_mae, data_nasc) VALUES (?, ?, ?, ?)"

sql_busca = "SELECT id FROM acolhidos WHERE cpf = ?"

def inserirAcolhido(nome, cpf, nome_mae, data_nasc):

    conexao, cursor   = conexaoDB.conectarDB()

    try:

        cursor.execute(f"""{sql_busca}""", (cpf,))
        resultado_pesquisa = cursor.fetchone()

        if resultado_pesquisa:
            log(f"Acolhido {nome}, já cadastrado no sistema. Inserindo na planilha de RETORNO.")

            return False

        if not resultado_pesquisa:    

            cursor.execute(f"""{sql_insert}""", (nome, cpf, nome_mae, data_nasc))

            conexao.commit()

            log(f"Acolhido {nome}, Adicionado com sucesso!")

            return True

    except Exception as e:
        log(f"Erro ao inserir o acolhido {nome}: {e}")

        return False

    finally:
        cursor.close()
        conexao.close()