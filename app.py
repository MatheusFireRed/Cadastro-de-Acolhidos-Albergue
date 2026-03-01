import tkinter as tk
import db.criarDB
from db import conexaoDB, InserirDB
from datetime import datetime
from functions.letrasMaiusculas import letrasMaiusculas
from functions.formatarCpf import formatarCpf
from functions.formatarData import formatarData
from functions.log import log

log("<=======================================================>")
log("Programa iniciado..")

#Data atual 
data_atual = datetime.now().strftime("%d/%m/%y")

db.criarDB.criarDB()

janelaPrincipal = tk.Tk()
janelaPrincipal.title("Acolhimento Pernoite")
janelaPrincipal.geometry("700x700")

#Subtitulo da página
subtitulo = tk.Label(janelaPrincipal, text="Cadastro de Acolhidos, Data: " + data_atual, font=("Arial", 20, "bold"))
subtitulo.pack(pady=30)

# Nome
txtNome = tk.Label(janelaPrincipal, text="Nome completo:")
txtNome.pack()
varNome = tk.StringVar()
varNome.trace_add("write", lambda *args: letrasMaiusculas(varNome))
inputNome = tk.Entry(janelaPrincipal, width=50, textvariable=varNome)
inputNome.pack()

# CPF
txtCpf = tk.Label(janelaPrincipal, text="CPF:")
txtCpf.pack()
inputCpf = tk.Entry(janelaPrincipal, width=50)
inputCpf.pack()
inputCpf.bind('<KeyRelease>', formatarCpf)

# Data de Nascimento
txtDataNasc = tk.Label(janelaPrincipal, text="Data de nascimento:")
txtDataNasc.pack()
inputDataNasc = tk.Entry(janelaPrincipal, width=50)
inputDataNasc.pack()
inputDataNasc.bind('<KeyRelease>', formatarData)  # <-- EXATAMENTE IGUAL AO CPF

# Nome da Mãe
txtNomeMae = tk.Label(janelaPrincipal, text="Nome completo da mãe:")
txtNomeMae.pack()
varNomeMae = tk.StringVar()
varNomeMae.trace_add("write", lambda *args: letrasMaiusculas(varNomeMae))
inputNomeMae = tk.Entry(janelaPrincipal, width=50, textvariable=varNomeMae)
inputNomeMae.pack()

def cadastrar():
    nome        = varNome.get().strip()
    cpf         = inputCpf.get().strip()
    data_nasc   = inputDataNasc.get().strip()
    nome_mae    = varNomeMae.get().strip()

    log("Dados coletados..")
    log("Dados passados para a funcao inserirAcolhido")
    InserirDB.inserirAcolhido(nome, cpf, data_nasc, nome_mae)

#Botão de cadastro
#COLOCAR command= mais a função de cadastro após 
btn_cadastro = tk.Button(janelaPrincipal,text="CADASTRAR", command=cadastrar, width=40, font=("Arial", 15, "bold"))
btn_cadastro.pack(pady=50)

janelaPrincipal.mainloop()

log("Programa encerrado!")
log("")
log("")
log("")
log("<=======================================================>")

