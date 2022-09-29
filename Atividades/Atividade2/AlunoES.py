from Aluno import Aluno

class AlunoES(Aluno):
    def __init__(self, cod, name, registration, semester):
        Aluno.__init__(self, cod, name, registration)
        self.semester = semester

    def imprimir(self):
        Aluno.imprimir(self)
        print('Semestre: ', self.semester)