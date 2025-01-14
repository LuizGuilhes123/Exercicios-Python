import random
import time

def gerar_precos_iniciais(acoes):
    return {acao: random.uniform(50, 500) for acao in acoes}

def atualizar_precos(precos):
    for acao in precos:
        variacao = random.uniform(-0.05, 0.05)  # Variação de até ±5%
        precos[acao] += precos[acao] * variacao
        precos[acao] = max(precos[acao], 1)  # Preço mínimo de 1
    return precos

def mostrar_portfolio(portfolio, precos):
    print("\n=== Seu Portfólio ===")
    total = 0
    for acao, quantidade in portfolio.items():
        valor = quantidade * precos[acao]
        print(f"Ação: {acao}, Quantidade: {quantidade}, Preço Atual: R${precos[acao]:.2f}, Valor: R${valor:.2f}")
        total += valor
    print(f"Valor Total do Portfólio: R${total:.2f}")
    return total

def main():
    acoes = ["TechCorp", "HealthInc", "FinanceLtd", "EnergyCo", "RetailGroup"]
    precos = gerar_precos_iniciais(acoes)
    portfolio = {acao: 0 for acao in acoes}
    saldo = 10000  # Saldo inicial fictício

    print("Bem-vindo ao Simulador de Mercado de Ações!")
    print(f"Seu saldo inicial: R${saldo:.2f}\n")

    while True:
        print("\n=== Mercado Atual ===")
        for acao, preco in precos.items():
            print(f"Ação: {acao}, Preço: R${preco:.2f}")

        print("\nOpções:")
        print("1. Comprar Ações")
        print("2. Vender Ações")
        print("3. Ver Portfólio")
        print("4. Passar o Dia")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            acao = input("Digite o nome da ação que deseja comprar: ")
            if acao not in precos:
                print("Ação inválida!")
                continue
            quantidade = int(input("Digite a quantidade que deseja comprar: "))
            custo = quantidade * precos[acao]
            if custo > saldo:
                print("Saldo insuficiente!")
            else:
                saldo -= custo
                portfolio[acao] += quantidade
                print(f"Você comprou {quantidade} ações de {acao} por R${custo:.2f}. Saldo restante: R${saldo:.2f}")

        elif opcao == "2":
            acao = input("Digite o nome da ação que deseja vender: ")
            if acao not in precos:
                print("Ação inválida!")
                continue
            quantidade = int(input("Digite a quantidade que deseja vender: "))
            if quantidade > portfolio[acao]:
                print("Quantidade insuficiente no portfólio!")
            else:
                receita = quantidade * precos[acao]
                saldo += receita
                portfolio[acao] -= quantidade
                print(f"Você vendeu {quantidade} ações de {acao} por R${receita:.2f}. Novo saldo: R${saldo:.2f}")

        elif opcao == "3":
            mostrar_portfolio(portfolio, precos)

        elif opcao == "4":
            print("Passando para o próximo dia...")
            time.sleep(1)
            precos = atualizar_precos(precos)

        elif opcao == "5":
            print("Obrigado por usar o Simulador de Mercado de Ações Python!")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
