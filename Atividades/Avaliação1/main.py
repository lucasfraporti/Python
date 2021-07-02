from Computador import Computador
from Desktop import Desktop
from Notebook import Notebook

TesteD = Desktop("Intel", "Preto", 5000, 750)
TesteD.cadastrar()
TesteD.getInformacoes()

TesteN = Notebook("Positivo", "Azul", 1900, 150)
TesteN.cadastrar()
TesteN.getInformacoes()
