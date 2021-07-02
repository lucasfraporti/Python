from veiculo import Veiculo

class Bicicleta():
    def __init__(self, marcaV, qtdRodasV, modeloV, velocidadeV, numMarchasB, bagageiroB):
        Veiculo.__init__(self, marcaV, qtdRodasV, modeloV, velocidadeV)
        self.numMarchas = numMarchasB
        self.bagageiro = bagageiroB

    def imprimirinformacoesB(self):
        print("-- Informações sobre a bicicleta -- \nMarca:", self.marca, "Total de rodas:", self.qtdRodas, "Modelo:", self.modelo, "Velocidade:", self.velocidade, "Número de marchas:", self.numMarchas, "Bagageiro:", self.bagageiro)