import tkinter as tk
from functions.letrasMaiusculas import letrasMaiusculas
from functions.formatarCpf import formatarCpf
from functions.formatarData import formatarData

janelaPrincipal = tk.Tk()
janelaPrincipal.title("Acolhimento Pernoite")
janelaPrincipal.geometry("500x500")

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

janelaPrincipal.mainloop()