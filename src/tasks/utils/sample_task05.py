class Veiculo:
    __total_veiculos = 0

    def __init__(self, nome, ano, valor_diario):
        self.__nome = nome
        self.__ano = ano
        self.__valor_diario = valor_diario
        Veiculo.__total_veiculos += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def valor_diario(self):
        return self.__valor_diario

    @valor_diario.setter
    def valor_diario(self, valor_diario):
        self.__valor_diario = valor_diario

    def calcular_aluguel(self, dias, desconto=0):
        valor_total = self.__valor_diario * dias * (1 - desconto)
        if dias > 7:
            valor_total *= 0.95
        return valor_total

    @classmethod
    def total_veiculos(cls):
        return cls.__total_veiculos

    @classmethod
    def aumentar_valor_diario(cls, percentual):
        cls.__valor_diario += cls.__valor_diario * (percentual / 100)


class Carro(Veiculo):
    def __init__(self, nome, ano, valor_diario, tipo_combustivel):
        super().__init__(nome, ano, valor_diario)
        self.tipo_combustivel = tipo_combustivel


class Moto(Veiculo):
    def __init__(self, nome, ano, valor_diario, cilindrada):
        super().__init__(nome, ano, valor_diario)
        self.cilindrada = cilindrada

    def calcular_aluguel(self, dias, desconto=0):
        valor_total = super().calcular_aluguel(dias, desconto)
        if self.cilindrada > 200:
            valor_total *= 1.10
        return valor_total


# Exemplos de uso
carro = Carro("Toyota Corolla", 2022, 150, "Gasolina")
moto = Moto("Yamaha XJ6", 2021, 80, 600)

print(f"Aluguel do carro por 10 dias: R${carro.calcular_aluguel(10, 0.1)}")
print(f"Aluguel da moto por 10 dias: R${moto.calcular_aluguel(10, 0.1)}")

print(f"Total de veículos cadastrados: {Veiculo.total_veiculos()}")
