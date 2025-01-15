import random

# Base de dados de alimentos
alimentos = {
    "café_da_manhã": [
        {"nome": "Aveia com frutas", "calorias": 250},
        {"nome": "Omelete com espinafre", "calorias": 200},
        {"nome": "Iogurte natural com granola", "calorias": 180},
        {"nome": "Panqueca de banana e aveia", "calorias": 220},
        {"nome": "Torradas integrais com abacate", "calorias": 240},
        {"nome": "Smoothie de frutas com proteína", "calorias": 300},
        {"nome": "Pão integral com ovo pochê", "calorias": 210},
        {"nome": "Crepioca recheada com queijo branco", "calorias": 230},
    ],
    "almoço": [
        {"nome": "Frango grelhado com legumes", "calorias": 400},
        {"nome": "Salada de quinoa com grão-de-bico", "calorias": 350},
        {"nome": "Peixe assado com batata doce", "calorias": 450},
        {"nome": "Macarrão integral com molho de tomate", "calorias": 370},
        {"nome": "Arroz integral, feijão e carne magra", "calorias": 430},
        {"nome": "Tofu com legumes ao molho shoyu", "calorias": 340},
        {"nome": "Estrogonofe de frango com arroz integral", "calorias": 410},
        {"nome": "Lasanha de berinjela", "calorias": 380},
    ],
    "jantar": [
        {"nome": "Sopa de lentilha", "calorias": 300},
        {"nome": "Wrap de frango com salada", "calorias": 320},
        {"nome": "Tofu grelhado com vegetais", "calorias": 280},
        {"nome": "Omelete de claras com abobrinha", "calorias": 200},
        {"nome": "Creme de abóbora com gengibre", "calorias": 250},
        {"nome": "Sanduíche natural de atum", "calorias": 290},
        {"nome": "Salada Caesar com frango grelhado", "calorias": 310},
        {"nome": "Arroz de couve-flor com cogumelos", "calorias": 270},
    ],
    "lanches": [
        {"nome": "Mix de castanhas", "calorias": 150},
        {"nome": "Fruta (maçã, banana, etc.)", "calorias": 100},
        {"nome": "Pão integral com pasta de amendoim", "calorias": 200},
        {"nome": "Barra de cereal", "calorias": 120},
        {"nome": "Iogurte grego com mel", "calorias": 130},
        {"nome": "Palitos de cenoura com homus", "calorias": 110},
        {"nome": "Bolachas integrais com queijo cottage", "calorias": 140},
        {"nome": "Smoothie verde com espinafre e kiwi", "calorias": 160},
    ],
}

def gerar_cardapio(dieta="equilibrada", calorias_totais=2000):
    print("\n--- Cardápio Planejado ---")
    calorias_por_refeicao = calorias_totais // 3
    total_calorias = 0

    for refeicao, opcoes in alimentos.items():
        if refeicao == "lanches":
            continue
        prato = random.choice(opcoes)
        if dieta == "vegano" and ("frango" in prato["nome"].lower() or "peixe" in prato["nome"].lower()):
            prato = {"nome": "Tofu com quinoa", "calorias": 360}  # Exemplo de substituição para veganos

        print(f"{refeicao.capitalize()}: {prato['nome']} - {prato['calorias']} kcal")
        total_calorias += prato["calorias"]

    # Lanches
    print("\nLanches:")
    while total_calorias < calorias_totais:
        lanche = random.choice(alimentos["lanches"])
        if total_calorias + lanche["calorias"] <= calorias_totais:
            print(f"- {lanche['nome']} - {lanche['calorias']} kcal")
            total_calorias += lanche["calorias"]
        else:
            break

    print(f"\nTotal estimado de calorias: {total_calorias} kcal")
    if total_calorias < calorias_totais:
        print(f"Ainda restam {calorias_totais - total_calorias} kcal para completar sua meta.")

def main():
    print("Bem-vindo ao Assistente de Planejamento de Refeições!")
    print("\nEscolha seu tipo de dieta:")
    print("1. Equilibrada")
    print("2. Vegano")
    print("3. Personalizado")

    opcao = input("Digite o número correspondente: ").strip()
    dieta = "equilibrada"
    if opcao == "2":
        dieta = "vegano"
    elif opcao == "3":
        print("Por enquanto, apenas as opções padrão estão disponíveis.")

    calorias_totais = int(input("Digite sua meta calórica diária (ex.: 3000): "))
    gerar_cardapio(dieta, calorias_totais)

if __name__ == "__main__":
    main()
