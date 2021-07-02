from veiculo import Veiculo

class Automovel():
    def __init__(self, marcaV, qtdRodasV, modeloV, velocidadeV, potenciadomotorA):
        Veiculo.__init__(self, marcaV, qtdRodasV, modeloV, velocidadeV)
        self.potenciadomotor = potenciadomotorA

    def imprimirinformacoesA(self):
        print("-- Informações sobre a bicicleta -- \nMarca:", self.marca, "Total de rodas:", self.qtdRodas, "Modelo:", self.modelo, "Velocidade:", self.velocidade, "Potência do motor:", self.potenciadomotor)