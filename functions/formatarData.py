def formatarData(event):
    # Pega o widget que gerou o evento
    widget = event.widget
    # Pega o texto atual
    texto = widget.get()
    
    # Remove tudo que não é número
    numeros = ''.join([c for c in texto if c.isdigit()])
    
    # Limita a 8 dígitos (DDMMAAAA)
    if len(numeros) > 8:
        numeros = numeros[:8]
    
    # Aplica a máscara da data (igual ao CPF)
    if len(numeros) <= 2:
        data_formatada = numeros
    elif len(numeros) <= 4:
        data_formatada = f"{numeros[:2]}/{numeros[2:]}"
    elif len(numeros) <= 8:
        data_formatada = f"{numeros[:2]}/{numeros[2:4]}/{numeros[4:8]}"
    else:
        data_formatada = f"{numeros[:2]}/{numeros[2:4]}/{numeros[4:8]}"
    
    # Atualiza o campo
    if texto != data_formatada:
        widget.delete(0, 'end')
        widget.insert(0, data_formatada)