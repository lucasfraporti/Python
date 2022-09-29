from Aluno import Aluno

class AlunoEM(Aluno):
    def __init__(self, cod, name, registration, year):
        Aluno.__init__(self, cod, name, registration)
        self.year = year

    def imprimir(self):
        Aluno.imprimir(self)
        print('Ano: ', self.year)