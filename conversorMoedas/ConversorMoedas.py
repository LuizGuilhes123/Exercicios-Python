import requests

# Função para obter as taxas de câmbio
def obter_taxas():
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    resposta = requests.get(url)
    dados = resposta.json()

    return dados["rates"]

# Função para converter o valor
def converter_moeda():
    print("Escolha a moeda de origem (BRL, USD, EUR):")
    moeda_origem = input().upper()

    print("Escolha a moeda de destino (BRL, USD, EUR):")
    moeda_destino = input().upper()

    print("Digite o valor a ser convertido:")
    valor = float(input())

    taxas = obter_taxas()

    if moeda_origem not in taxas or moeda_destino not in taxas:
        print("Moeda inválida. Tente novamente.")
        return

    # Convertendo para BRL primeiro, depois para a moeda de destino
    valor_em_brl = valor / taxas[moeda_origem]
    valor_convertido = valor_em_brl * taxas[moeda_destino]

    print(f"{valor} {moeda_origem} é igual a {valor_convertido:.2f} {moeda_destino}.")

def menu():
    while True:
        print("\nConversor de Moeda - Escolha uma opção:")
        print("1. Converter moeda")
        print("0. Sair")

        opcao = input("Digite sua opção: ")

        if opcao == "1":
            converter_moeda()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
