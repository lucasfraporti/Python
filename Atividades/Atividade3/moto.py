from automovel import Automovel

class Moto():
    def __init__(self, marcaV, qtdRodasV, modeloV, velocidadeV, potenciadomotorA, partidaEletricaM):
        Automovel.__init__(self, marcaV, qtdRodasV, modeloV, velocidadeV, potenciadomotorA)
        self.partidaeletrica = partidaEletricaM

    def imprimirinformacoesM(self):
        print("-- Informações sobre a motocicleta -- \nMarca:", self.marca, "Total de rodas:", self.qtdRodas, "Modelo:", self.modelo, "Velocidade:", self.velocidade, "Potência do motor:", self.potenciadomotor, "Partida elétrica:", self.partidaeletrica)