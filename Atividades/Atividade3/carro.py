from automovel import Automovel

class Carro():
    def __init__(self, marcaV, qtdRodasV, modeloV, velocidadeV, potenciadomotorA, qtdPortasC):
        Automovel.__init__(self, marcaV, qtdRodasV, modeloV, velocidadeV, potenciadomotorA)
        self.qtdPortas = qtdPortasC

    def imprimirinformacoesC(self):
        print("-- Informações sobre o carro -- \nMarca:", self.marca, "Total de rodas:", self.qtdRodas, "Modelo:", self.modelo, "Velocidade:", self.velocidade, "Potência do motor:", self.potenciadomotor, "Total de portas:", self.qtdPortas)