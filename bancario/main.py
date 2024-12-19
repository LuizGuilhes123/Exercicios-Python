import textwrap

# Constantes
LIMITE_SAQUES = 3
LIMITE_SAQUE_VALOR = 500
AGENCIA = "0001"

# Funções de exibição
def menu():
    opcoes = """
    ======= MENU =======

        [d]  Depositar
        [s]  Sacar
        [e]  Extrato
        [nu] Novo Usuário
        [nc] Nova Conta
        [lc] Listar Contas
        [lu] Listar Usuários
        [f]  Fim/Sair
    => """
    return input(textwrap.dedent(opcoes))

def exibir_mensagem(msg):
    print(f"\n{msg}\n")

# Funções bancárias
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        exibir_mensagem("=== Depósito realizado com sucesso! ===")
    else:
        exibir_mensagem("### Operação falhou! Valor inválido. ###")

    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques):
    if valor <= 0:
        exibir_mensagem("### Operação falhou! Valor inválido. ###")
    elif valor > saldo:
        exibir_mensagem("### Operação falhou! Saldo insuficiente. ###")
    elif valor > limite:
        exibir_mensagem("### Operação falhou! Valor excede o limite. ###")
    elif numero_saques >= LIMITE_SAQUES:
        exibir_mensagem("### Operação falhou! Limite de saques diários atingido. ###")
    else:
        saldo -= valor
        extrato.append(f"Saque:    R$ {valor:.2f}")
        numero_saques += 1
        exibir_mensagem("=== Saque realizado com sucesso! ===")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n======= Extrato =======")
    if extrato:
        print("\n".join(extrato))
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo:    R$ {saldo:.2f}")
    print("=======================")

# Funções de usuários e contas
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(u["cpf"] == cpf for u in usuarios):
        exibir_mensagem("### Já existe usuário com esse CPF! ###")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    exibir_mensagem("=== Usuário criado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if usuario:
        exibir_mensagem("=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    exibir_mensagem("### Usuário não encontrado. Cadastre o usuário primeiro. ###")
    return None

def listar_contas(contas):
    if not contas:
        exibir_mensagem("### Não há contas cadastradas. ###")
        return

    for conta in contas:
        print("=" * 40)
        print(f"Agência:    {conta['agencia']}")
        print(f"C/C:        {conta['numero_conta']}")
        print(f"Titular:    {conta['usuario']['nome']}")
        print("=" * 40)

def listar_usuarios(usuarios):
    if not usuarios:
        exibir_mensagem("### Não há usuários cadastrados. ###")
        return

    for usuario in usuarios:
        print("=" * 40)
        print(f"Nome:       {usuario['nome']}")
        print(f"CPF:        {usuario['cpf']}")
        print(f"Endereço:   {usuario['endereco']}")
        print("=" * 40)

# Função principal
def main():
    saldo = 0
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, LIMITE_SAQUE_VALOR, numero_saques)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "lu":
            listar_usuarios(usuarios)

        elif opcao == "f":
            exibir_mensagem("Saindo do sistema. Até logo!")
            break

        else:
            exibir_mensagem("### Opção inválida! Tente novamente. ###")

if __name__ == "__main__":
    main()
