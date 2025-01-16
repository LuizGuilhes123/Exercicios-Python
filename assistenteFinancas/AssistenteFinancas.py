import os
import pickle
from datetime import datetime

ARQUIVO_FINANCAS = "financas.pkl"

class PlanejamentoFinanceiro:
    def __init__(self):
        self.financas = {
            "transacoes": [],
            "orcamento": {}
        }
        self.carregar_dados()

    def salvar_dados(self):
        """Salva os dados financeiros no arquivo."""
        with open(ARQUIVO_FINANCAS, "wb") as arquivo:
            pickle.dump(self.financas, arquivo)

    def carregar_dados(self):
        """Carrega os dados financeiros do arquivo."""
        if os.path.exists(ARQUIVO_FINANCAS):
            with open(ARQUIVO_FINANCAS, "rb") as arquivo:
                self.financas = pickle.load(arquivo)

    def adicionar_transacao(self):
        """Adiciona uma nova transação."""
        tipo = self.obter_tipo_transacao()
        valor = self.obter_valor_transacao(tipo)
        categoria = input("Digite a categoria (ex: alimentação, transporte, lazer, etc.): ").strip()
        descricao = input("Digite uma descrição para a transação (opcional): ").strip()

        self.financas["transacoes"].append({
            "tipo": tipo,
            "valor": valor,
            "categoria": categoria,
            "descricao": descricao,
            "data": datetime.now()
        })

        print("Transação registrada com sucesso!\n")

    def obter_tipo_transacao(self):
        tipo = input("Digite o tipo da transação (receita ou despesa): ").strip().lower()
        while tipo not in ["receita", "despesa"]:
            print("Tipo inválido! Escolha 'receita' ou 'despesa'.")
            tipo = input("Digite o tipo da transação (receita ou despesa): ").strip().lower()
        return tipo

    def obter_valor_transacao(self, tipo):
        while True:
            try:
                valor = float(input("Digite o valor da transação: R$ "))
                if tipo == "despesa" and valor < 0:
                    print("Erro: Despesas não podem ter valor negativo.")
                elif tipo == "receita" and valor <= 0:
                    print("Erro: Receitas precisam ter valor positivo.")
                else:
                    return valor
            except ValueError:
                print("Valor inválido! Digite um número.")

    def definir_orcamento(self):
        """Define o orçamento para uma categoria."""
        categoria = input("Digite a categoria para definir o orçamento: ").strip()
        limite = float(input(f"Digite o limite de orçamento para {categoria} (R$): "))
        self.financas["orcamento"][categoria] = limite
        print(f"Orçamento para '{categoria}' definido como R$ {limite:.2f}.\n")

    def exibir_relatorio(self):
        """Exibe o relatório financeiro mensal."""
        receitas = sum(t["valor"] for t in self.financas["transacoes"] if t["tipo"] == "receita")
        despesas = sum(t["valor"] for t in self.financas["transacoes"] if t["tipo"] == "despesa")
        saldo = receitas - despesas

        print("\n--- Relatório Financeiro Mensal ---")
        print(f"Receitas totais: R$ {receitas:.2f}")
        print(f"Despesas totais: R$ {despesas:.2f}")
        print(f"Saldo final: R$ {saldo:.2f}\n")

        if despesas > receitas:
            print("⚠️ Atenção: Você gastou mais do que recebeu este mês. Considere ajustar suas despesas.\n")
        else:
            print("✅ Bom trabalho! Você está gastando dentro do seu orçamento.\n")

        self.exibir_despesas_por_categoria()

    def exibir_despesas_por_categoria(self):
        """Exibe as despesas por categoria."""
        categorias = {}
        for t in self.financas["transacoes"]:
            if t["tipo"] == "despesa":
                categorias[t["categoria"]] = categorias.get(t["categoria"], 0) + t["valor"]

        print("--- Despesas por Categoria ---")
        for categoria, total in categorias.items():
            limite = self.financas["orcamento"].get(categoria)
            print(f"- {categoria}: R$ {total:.2f}", end="")

            if limite:
                print(f" (Orçamento: R$ {limite:.2f})", end="")
                if total > limite:
                    print(" ⚠️ Excedido!")
                else:
                    print(" ✅ Dentro do orçamento.")
            else:
                print(" (Sem orçamento definido)")

    def alterar_nome_categoria(self):
        """Altera o nome de uma categoria."""
        categoria_antiga = input("Digite o nome da categoria que deseja alterar: ").strip()
        if categoria_antiga in self.financas["orcamento"]:
            categoria_nova = input("Digite o novo nome para a categoria: ").strip()
            # Atualizando o nome da categoria no orçamento
            self.financas["orcamento"][categoria_nova] = self.financas["orcamento"].pop(categoria_antiga)

            # Atualizando as transações associadas à categoria
            for transacao in self.financas["transacoes"]:
                if transacao["categoria"] == categoria_antiga:
                    transacao["categoria"] = categoria_nova

            print(f"A categoria '{categoria_antiga}' foi renomeada para '{categoria_nova}'.\n")
            self.salvar_dados()
        else:
            print(f"A categoria '{categoria_antiga}' não existe no orçamento.\n")

    def alterar_orcamento_categoria(self):
        """Altera o orçamento de uma categoria."""
        categoria = input("Digite a categoria para a qual deseja alterar o orçamento: ").strip()
        if categoria in self.financas["orcamento"]:
            novo_orcamento = float(input(f"Digite o novo valor de orçamento para '{categoria}': R$ "))
            self.financas["orcamento"][categoria] = novo_orcamento
            print(f"O orçamento para '{categoria}' foi alterado para R$ {novo_orcamento:.2f}.\n")
            self.salvar_dados()
        else:
            print(f"A categoria '{categoria}' não existe no orçamento.\n")

    def menu(self):
        """Menu principal do programa."""
        while True:
            print("\n=== Assistente de Planejamento Financeiro ===")
            print("1. Adicionar Transação")
            print("2. Definir Orçamento por Categoria")
            print("3. Exibir Relatório Financeiro")
            print("4. Alterar Nome de Categoria")
            print("5. Alterar Orçamento de Categoria")
            print("6. Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.adicionar_transacao()
            elif opcao == "2":
                self.definir_orcamento()
            elif opcao == "3":
                self.exibir_relatorio()
            elif opcao == "4":
                self.alterar_nome_categoria()
            elif opcao == "5":
                self.alterar_orcamento_categoria()
            elif opcao == "6":
                self.salvar_dados()
                print("Saindo do Assistente de Planejamento Financeiro. Até logo!")
                break
            else:
                print("Opção inválida! Tente novamente.\n")


if __name__ == "__main__":
    app = PlanejamentoFinanceiro()
    app.menu()
