def deletar_estudo(nome_arquivo="dados_estudo.txt"):
    """
    Permite ao usuário visualizar as matérias existentes e escolher 
    entre deletar o histórico de uma matéria específica ou limpar 
    todo o arquivo de dados.
    """
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
    
    materias = [linha.split(",")[0].split(": ")[1] for linha in linhas]
    materias_unicas = set(materias)
    
    print("Matérias disponíveis para deletar:")
    for i, materia in enumerate(materias_unicas, 1):
        print(f"{i}. {materia}")
    print(f"{len(materias_unicas) + 1}. Deletar todo o histórico")
    
    escolha = int(input("Escolha uma opção: "))
    
    if escolha == len(materias_unicas) + 1:
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write("")
        print("Todo o histórico foi deletado.")
    elif 1 <= escolha <= len(materias_unicas):
        materia_para_deletar = list(materias_unicas)[escolha - 1]
        linhas_filtradas = [linha for linha in linhas if materia_para_deletar not in linha]
        
        with open(nome_arquivo, "w") as arquivo:
            arquivo.writelines(linhas_filtradas)
        
        print(f"O histórico da matéria '{materia_para_deletar}' foi deletado.")
    else:
        print("Opção inválida. Por favor, escolha novamente.")
