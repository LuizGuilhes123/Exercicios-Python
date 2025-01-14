import random
import string

def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_numeros=True, incluir_especiais=True):
    caracteres = string.ascii_lowercase
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def verificar_forca(senha):
    pontos = 0
    if len(senha) >= 8:
        pontos += 1
    if any(c.islower() for c in senha):
        pontos += 1
    if any(c.isupper() for c in senha):
        pontos += 1
    if any(c.isdigit() for c in senha):
        pontos += 1
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for c in senha):
        pontos += 1

    if pontos <= 2:
        return "Fraca"
    elif pontos == 3:
        return "Moderada"
    else:
        return "Forte"

def obter_inteiro(mensagem, minimo):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit() and int(entrada) >= minimo:
            return int(entrada)
        else:
            print(f"Por favor, insira um número inteiro maior ou igual a {minimo}.")

def main():
    print("Bem-vindo ao Gerador de Senhas Seguras!")
    comprimento = obter_inteiro("Digite o comprimento desejado da senha (mínimo 8): ", 8)

    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").strip().lower() == 's'
    incluir_especiais = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'

    senha = gerar_senha(comprimento, incluir_maiusculas, incluir_numeros, incluir_especiais)
    forca = verificar_forca(senha)

    print("\nSenha gerada:", senha)
    print("Força da senha:", forca)

if __name__ == "__main__":
    main()
