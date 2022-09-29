from Aluno import Aluno
from AlunoEM import AlunoEM
from AlunoES import AlunoES

if __name__ == '__main__':
    Aluninho = Aluno("01", "Carlos Souza", "1010")
    Aluninho.imprimir()
    print("="*20)
    AluninhoEM = AlunoEM("02", "Bernardo Azevedo", "2020", "9º ano")
    AluninhoEM.imprimir()
    print("="*20)
    AluninhoES = AlunoES("03", "Elton Munhoz", "1000", "5º semestre")
    AluninhoES.imprimir()