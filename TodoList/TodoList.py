import time
import os
import pickle
from datetime import datetime

# Arquivo para salvar tarefas
ARQUIVO_TAREFAS = "tarefas.pkl"

# Lista para armazenar as tarefas
tarefas = []

def salvar_tarefas():
    """Salva as tarefas no arquivo."""
    with open(ARQUIVO_TAREFAS, "wb") as arquivo:
        pickle.dump(tarefas, arquivo)

def carregar_tarefas():
    """Carrega as tarefas do arquivo."""
    global tarefas
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "rb") as arquivo:
            tarefas = pickle.load(arquivo)

def adicionar_tarefa():
    """Adiciona uma nova tarefa à lista de tarefas."""
    nome = input("Digite o nome da tarefa: ").strip()
    prioridade = input("Digite a prioridade (alta, média, baixa): ").strip().lower()

    while prioridade not in ["alta", "média", "media", "baixa"]:
        print("Prioridade inválida! Escolha entre alta, média ou baixa.")
        prioridade = input("Digite a prioridade (alta, média, baixa): ").strip().lower()

    tarefas.append({"nome": nome, "prioridade": prioridade, "data": datetime.now()})
    salvar_tarefas()
    print(f"Tarefa '{nome}' adicionada com sucesso!\n")

def listar_tarefas():
    """Lista todas as tarefas com suas prioridades."""
    if not tarefas:
        print("Nenhuma tarefa encontrada!\n")
        return

    print("\n--- Tarefas ---")
    tarefas_ordenadas = sorted(tarefas, key=lambda t: t["prioridade"], reverse=True)
    for i, tarefa in enumerate(tarefas_ordenadas, 1):
        print(f"{i}. {tarefa['nome']} (Prioridade: {tarefa['prioridade']}, Adicionada em: {tarefa['data'].strftime('%Y-%m-%d %H:%M:%S')})")
    print()

def iniciar_timer_pomodoro():
    """Inicia um ciclo Pomodoro com personalização do usuário."""
    try:
        foco = int(input("Digite o tempo de foco em minutos (padrão 25): ") or 25)
        descanso = int(input("Digite o tempo de descanso em minutos (padrão 5): ") or 5)
    except ValueError:
        print("Entrada inválida! Usando os valores padrão (25 minutos de foco e 5 minutos de descanso).")
        foco, descanso = 25, 5

    print("\nIniciando ciclo Pomodoro!")
    print(f"{foco} minutos de foco começam agora...")

    # Timer de foco
    for i in range(foco, 0, -1):
        print(f"Tempo restante: {i} minutos", end="\r")
        time.sleep(60)

    print("\nTempo de foco acabou! Agora descanse por {descanso} minutos.")

    # Timer de descanso
    for i in range(descanso, 0, -1):
        print(f"Tempo restante de descanso: {i} minutos", end="\r")
        time.sleep(60)

    print("\nCiclo Pomodoro finalizado! Você está pronto para começar outra tarefa.\n")

def remover_tarefa():
    """Remove uma tarefa da lista."""
    listar_tarefas()
    if not tarefas:
        return

    try:
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            salvar_tarefas()
            print(f"Tarefa '{tarefa_removida['nome']}' removida com sucesso!\n")
        else:
            print("Número inválido!\n")
    except ValueError:
        print("Entrada inválida! Digite um número válido.\n")

def notificar_usuario(mensagem):
    """Exibe uma notificação simples no terminal."""
    print(f"\a{mensagem}")  # \a emite um som de alerta no terminal

def menu():
    """Menu principal do programa."""
    carregar_tarefas()
    while True:
        print("=== Organizador de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Iniciar Timer Pomodoro")
        print("4. Remover Tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            iniciar_timer_pomodoro()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            print("Saindo do Organizador de Tarefas. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    menu()
    