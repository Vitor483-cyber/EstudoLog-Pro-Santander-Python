def salvar_dados(dados, nome_arquivo="dados_estudo.txt"):
    """
    Recebe um dicionário com as informações do estudo e as anexa
    em um arquivo de texto para persistência permanente.
    """
    with open(nome_arquivo, "a") as arquivo:
        linha = f"Matéria: {dados['materia']}, Tempo de Estudo: {dados['tempo_estudo']} horas\n"
        arquivo.write(linha)    

def ler_dados(nome_arquivo="dados_estudo.txt"):
    """
    Lê o arquivo de histórico, exibe cada registro no terminal e 
    gera um relatório de matérias únicas utilizando a lógica de Sets.
    """
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print("Nenhum registro de estudo encontrado.")
                return
            
            for linha in linhas:
                print(linha.strip())
        
        materias_unicas = set()
        for linha in linhas:
            materia = linha.split(",")[0].split(": ")[1]
            materias_unicas.add(materia)
        
        print("Matérias únicas estudadas:")
        for materia in materias_unicas:
            print(f"- {materia}")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Comece registrando seus estudos!")
