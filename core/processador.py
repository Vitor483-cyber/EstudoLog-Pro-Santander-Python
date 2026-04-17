def processar_dados():
    """
    Solicita ao usuário o nome da matéria e o tempo de estudo.
    Possui tratamento de exceção (ValueError) para garantir que o tempo 
    seja um número válido e retorna um dicionário formatado.
    """
    dados_estudo = {}
    
    while True:
        try:
            materia = input("Digite o nome da matéria: ")
            tempo_estudo = float(input("Digite o tempo de estudo em horas: "))
            dados_estudo['materia'] = materia
            dados_estudo['tempo_estudo'] = tempo_estudo
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o tempo de estudo.")
    
    return dados_estudo