class Veiculo:
    def __init__(self, marca, ano):
        self._marca = marca
        self._ano = ano

    def apresentar(self):
        print(f"Marca: {self._marca}, Ano: {self._ano}")

class Carro(Veiculo):
    def __init__(self, marca, ano, numero_portas):
        super().__init__(marca, ano)
        self._numero_portas = numero_portas

    def apresentar(self):
        super().apresentar()
        print(f"Número de portas: {self._numero_portas}")

class Moto(Veiculo):
    def __init__(self, marca, ano, tipo):
        super().__init__(marca, ano)
        self._tipo = tipo

    def apresentar(self):
        super().apresentar()
        print(f"Tipo: {self._tipo}")

def main():
    print("Digite o tipo do veículo (carro/moto):")
    tipo = input()

    print("Digite a marca do veículo:")
    marca = input()

    print("Digite o ano de fabricação do veículo:")
    ano = int(input())

    if tipo == 'carro':
        print("Digite o número de portas do carro:")
        numero_portas = int(input())
        veiculo = Carro(marca, ano, numero_portas)
    elif tipo == 'moto':
        print("Digite o tipo de moto:")
        tipo = input()
        veiculo = Moto(marca, ano, tipo)
    else:
        print("Tipo de veículo inválido. Tente novamente.")
        return

    veiculo.apresentar()

if __name__ == '__main__':
    main()
