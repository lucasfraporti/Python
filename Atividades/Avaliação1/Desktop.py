from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco = 0, potenciaDaFonte = 0):
        self._modelo = modelo
        self._cor = cor
        if preco > 0 :
            self._preco = preco
        else:
            self._preco = 0
        self._potenciaDaFonte = potenciaDaFonte
    
    @property
    def modelo(self):
        return self._modelo

    @property
    def cor(self):
        return self._cor

    @property
    def preco(self):
        return self._preco

    @property
    def potenciaDaFonte(self):
        return self._potenciaDaFonte

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @preco.setter
    def preco(self, preco):
        if preco >= 0 :
            self._preco = preco
        else:
            print("Valor inválido!")

    @potenciaDaFonte.setter
    def potenciaDaFonte(self, potenciaDaFonte):
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        print(self._modelo, self._cor, self._preco, self._potenciaDaFonte)
    
    def cadastrar(self):
        return print("Cadastrado!")