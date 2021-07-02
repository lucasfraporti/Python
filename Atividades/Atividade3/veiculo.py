class Veiculo():
    def __init__(self, marcaV, qtdRodasV, modeloV, velocidadeV = 0):
        self.marca = marcaV
        self.qtdRodas = qtdRodasV
        self.modelo = modeloV
        self.velocidade = velocidadeV

    def imprimirinformacoesV(self):
        print("-- Informações sobre o veículo -- \nMarca:", self.marca, "Total de rodas:", self.qtdRodas, "Modelo:", self.modelo, "Velocidade:", self.velocidade)

    def acelerarV(self, aceleracaoV):
        self.aceleracao = aceleracaoV
        self.velocidade = self.velocidade + aceleracaoV
        print(self.velocidade)

    def desacelerarV(self, desaceleracaoV):
        self.desaceleracao = desaceleracaoV
        self.velocidade = self.velocidade - desaceleracaoV
        print(self.velocidade)
