from abc import ABCMeta, abstractmethod

class Computador(metaclass=ABCMeta):
    @property
    def modelo(self):
        pass
    
    @property
    def cor(self):
        pass
    
    @property
    def preco(self):
        pass

    @modelo.setter
    @cor.setter
    @preco.setter

    @abstractmethod
    def cadastrar(self):       
        pass

    def getInformacoes(self, modelo, cor, preco):
        pass