class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self):
        tarefa = input("Digite a tarefa: ")
        self.tarefas.append(tarefa)
        print(f'Tarefa "{tarefa}" adicionada!')

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa.")
        else:
            for i, tarefa in enumerate(self.tarefas, 1):
                print(f"{i}. {tarefa}")

    def remover_tarefa(self):
        self.listar_tarefas()
        try:
            num = int(input("Número da tarefa para remover: "))
            if 1 <= num <= len(self.tarefas):
                removed = self.tarefas.pop(num - 1)
                print(f'Tarefa "{removed}" removida!')
            else:
                print("Erro. Tarefa não localizada.")
        except ValueError:
            print("Erro. Entrada inválida.")

    def executar(self):
        opcoes = {
            '1': self.adicionar_tarefa,
            '2': self.listar_tarefas,
            '3': self.remover_tarefa,
            '4': exit
        }

        while True:
            print("\n1. Adicionar Tarefa\n2. Listar Tarefas\n3. Remover Tarefa\n4. Sair")
            escolha = input("Escolha uma das opções acima: ")
            acao = opcoes.get(escolha, lambda: print("Opção inválida."))
            acao()

if __name__ == "__main__":
    app = GerenciadorTarefas()
    app.executar()