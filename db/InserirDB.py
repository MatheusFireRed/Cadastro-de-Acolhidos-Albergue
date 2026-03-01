from db import conexaoDB
from functions.log import log
from datetime import datetime

# APENAS PARA TESTES
data_atual = "01/01/2001"

sql_insert_acolhidos = "INSERT INTO acolhidos (nome, cpf, nome_mae, data_nasc) VALUES (?, ?, ?, ?)"
sql_insert_retornos  = "INSERT INTO retornos (id_acolhido, data_retorno) VALUES (?, ?)"
sql_busca_por_cpf    = "SELECT id, nome FROM acolhidos WHERE cpf = ?"  # Busca ID e NOME juntos

def inserirAcolhido(nome, cpf, nome_mae, data_nasc):
    conexao, cursor = conexaoDB.conectarDB()
    
    try:
        # Busca se o acolhido já existe pelo CPF
        cursor.execute(sql_busca_por_cpf, (cpf,))
        resultado = cursor.fetchone()
        
        if resultado:  # Já existe
            id_acolhido = resultado[0]      # Primeiro campo: id
            nome_existente = resultado[1]    # Segundo campo: nome
            
            log(f"Acolhido {nome_existente} (ID: {id_acolhido}) já cadastrado. Inserindo na tabela RETORNO.")
            
            # Insere o retorno
            cursor.execute(sql_insert_retornos, (id_acolhido, data_atual))
            conexao.commit()
            
            log(f"Retorno do acolhido {nome_existente} (ID: {id_acolhido}) adicionado!")
            return False
            
        else:  # Novo acolhido
            cursor.execute(sql_insert_acolhidos, (nome, cpf, nome_mae, data_nasc))
            conexao.commit()
            
            log(f"Acolhido {nome} adicionado com sucesso!")
            return True
            
    except Exception as e:
        log(f"Erro ao inserir o acolhido {nome}: {e}")
        conexao.rollback()  # Importante: desfaz alterações em caso de erro
        return False
        
    finally:
        cursor.close()
        conexao.close()