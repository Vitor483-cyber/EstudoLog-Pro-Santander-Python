
from core import processador, persistencia, deletar
import datetime
import random

def main():
    """
    Função principal que gerencia o loop do menu, coordena as chamadas 
    entre os módulos de processamento e persistência, e utiliza 
    o módulo datetime para registros temporais.
    """
    feedbacks = [
        "Ótimo trabalho! Continue assim!",
        "Você está progredindo muito bem!",
        "Excelente dedicação! Mantenha o ritmo!",
        "Parabéns pelo esforço! Você está no caminho certo!",
        "Incrível! Cada passo conta!"
    ]
    
    while True:
        print("\nMenu:")
        print("1. Registrar Estudo")
        print("2. Ver Histórico")
        print("3. Sair")
        print("4. Deletar Histórico")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            dados = processador.processar_dados()
            dados['data'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            persistencia.salvar_dados(dados)
            feedback = random.choice(feedbacks)
            print(feedback)
        
        elif escolha == '2':
            persistencia.ler_dados()
        
        elif escolha == '3':
            print("Saindo do programa. Até mais!")
            break
        
        elif escolha == '4':
            deletar.deletar_estudo()

        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()  

