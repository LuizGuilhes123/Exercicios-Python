import re

class ValidadorCPF:
    @staticmethod
    def extrair_digitos(cpf):
        return [int(digito) for digito in cpf if digito.isdigit()]

    @staticmethod
    def validar_formatacao(cpf):
        return bool(re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf) or re.match(r'\d{11}', cpf))

    @staticmethod
    def calcular_digito(cpf_numeros, multiplicadores):
        soma_produtos = sum(a * b for a, b in zip(cpf_numeros, multiplicadores))
        return (soma_produtos * 10 % 11) % 10

    @staticmethod
    def determinar_estado_origem(digito):
        estados = {
            1: "Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins",
            2: "Pará, Amazonas, Acre, Amapá, Rondônia ou Roraima",
            3: "Ceará, Maranhão ou Piauí",
            4: "Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas",
            5: "Bahia ou Sergipe",
            6: "Minas Gerais",
            7: "Rio de Janeiro ou Espírito Santo",
            8: "São Paulo",
            9: "Paraná ou Santa Catarina"
        }
        return estados.get(digito, "Rio Grande do Sul")

    def validar(self, cpf):
        numeros = self.extrair_digitos(cpf)

        if len(numeros) != 11:
            return False, "Quantidade de dígitos inválida."

        if not self.validar_formatacao(cpf):
            return False, "Formato do CPF inválido."

        primeiro_digito = self.calcular_digito(numeros[0:9], range(10, 1, -1))
        segundo_digito = self.calcular_digito(numeros[0:10], range(11, 1, -1))

        if numeros[9] != primeiro_digito or numeros[10] != segundo_digito:
            return False, "Dígitos verificadores não conferem."

        estado_origem = self.determinar_estado_origem(numeros[8])
        return True, estado_origem

    def executar(self):
        cpf = input("Digite um CPF para ser validado: ")
        valido, mensagem = self.validar(cpf)

        if valido:
            print(f"O CPF {cpf} é válido.")
            print(f"Seu CPF é originário do estado de {mensagem}.")
        else:
            print(f"O CPF {cpf} não é válido. {mensagem}")

if __name__ == "__main__":
    validador = ValidadorCPF()
    validador.executar()
