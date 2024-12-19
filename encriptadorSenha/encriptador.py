def encriptar():
    # Define o mapeamento de substituições em um dicionário
    substituicoes = {
        "0": "W",
        "1": "#",
        "2": "Z",
        "3": "%",
        "4": "X",
        "5": "@",
        "6": "&",
        "7": "K",
        "8": "H",
        "9": "?",
    }

    senha = input("Digite sua senha numérica para ENCRIPTAR...")
    listaSenha = list(senha)

    # Troca os números pelos caracteres com base no mapeamento
    listaSenha = [substituicoes.get(letra, letra) for letra in listaSenha]

    # Embaralha alguns caracteres usando atribuições diretas
    listaSenha[0], listaSenha[-1] = listaSenha[-1], listaSenha[0]
    listaSenha[2], listaSenha[-3] = listaSenha[-3], listaSenha[2]

    senha_encriptada = "".join(listaSenha)
    print(f"Sua senha encriptografada é: {senha_encriptada}")

encriptar()
