import time
from datetime import datetime

# Dicionário para armazenar as tarefas e o tempo gasto nelas
tarefas = {}

def iniciar_tarefa():
    """Inicia o temporizador para uma tarefa."""
    nome_tarefa = input("Digite o nome da tarefa: ").strip()
    tempo_inicial = time.time()  # Marca o início da tarefa

    print(f"Tarefa '{nome_tarefa}' iniciada. Digite 'sair' para finalizar.\n")

    while True:
        comando = input("Digite 'sair' para parar ou pressione Enter para continuar: ").strip().lower()
        if comando == "sair":
            tempo_final = time.time()  # Marca o fim da tarefa
            tempo_gasto = tempo_final - tempo_inicial  # Calcula o tempo gasto
            if nome_tarefa not in tarefas:
                tarefas[nome_tarefa] = 0
            tarefas[nome_tarefa] += tempo_gasto  # Adiciona o tempo à tarefa
            print(f"Tarefa '{nome_tarefa}' finalizada. Tempo gasto: {tempo_gasto/60:.2f} minutos.")
            break
        else:
            print("Tarefa em andamento...\n")

def exibir_relatorio():
    """Exibe o relatório de produtividade com o tempo gasto em cada tarefa."""
    if not tarefas:
        print("Nenhuma tarefa registrada.")
        return

    print("\n--- Relatório de Produtividade ---")
    for tarefa, tempo in tarefas.items():
        print(f"- {tarefa}: {tempo/60:.2f} minutos")

def menu():
    while True:
        print("\n=== Monitor de Produtividade ===")
        print("1. Iniciar uma nova tarefa")
        print("2. Exibir relatório de produtividade")
        print("3. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            iniciar_tarefa()
        elif opcao == "2":
            exibir_relatorio()
        elif opcao == "3":
            print("Saindo do Monitor de Produtividade. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

# Iniciar programa
if __name__ == "__main__":
    menu()
