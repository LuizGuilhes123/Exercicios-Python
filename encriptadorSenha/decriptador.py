def desencriptar():
    # Define o mapeamento de substituições em um dicionário
    substituicoes = {
        "W": "0",
        "#": "1",
        "Z": "2",
        "%": "3",
        "X": "4",
        "@": "5",
        "&": "6",
        "k": "7",
        "H": "8",
        "?": "9",
    }

    senha = input("Digite sua senha ENCRIPTADA PARA DESENCRIPTAR...")
    listaSenha = list(senha)

    # Desembaraça alguns caracteres usando atribuições diretas
    listaSenha[0], listaSenha[-1] = listaSenha[-1], listaSenha[0]
    listaSenha[2], listaSenha[-3] = listaSenha[-3], listaSenha[2]

    # Troca os caracteres com base no mapeamento
    listaSenha = [substituicoes.get(letra, letra) for letra in listaSenha]

    senha_desencriptada = "".join(listaSenha)
    print(f"Sua senha desencriptografada é: {senha_desencriptada}")

desencriptar()
