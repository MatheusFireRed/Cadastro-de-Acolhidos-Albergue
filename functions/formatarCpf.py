def formatarCpf(event):
    # Pega o widget que gerou o evento
    widget = event.widget
    # Pega o texto atual
    texto = widget.get()
    
    # Remove tudo que não é número
    numeros = ''.join([c for c in texto if c.isdigit()])
    
    # Limita a 11 dígitos
    if len(numeros) > 11:
        numeros = numeros[:11]
    
    # Aplica a máscara do CPF
    if len(numeros) <= 3:
        cpf_formatado = numeros
    elif len(numeros) <= 6:
        cpf_formatado = f"{numeros[:3]}.{numeros[3:]}"
    elif len(numeros) <= 9:
        cpf_formatado = f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:]}"
    else:
        cpf_formatado = f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:11]}"
    
    # Atualiza o campo
    if texto != cpf_formatado:
        widget.delete(0, 'end')
        widget.insert(0, cpf_formatado)