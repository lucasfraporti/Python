from Aluno import Aluno

class AlunoES(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        Aluno.imprimir(self)
        print('Semestre: ', self.semestre)