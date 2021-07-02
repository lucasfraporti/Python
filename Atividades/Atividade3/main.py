from automovel import Automovel
from bicicleta import Bicicleta
from carro import Carro
from moto import Moto
from veiculo import Veiculo

veh = Veiculo("Marca", "Rodas", "Modelo", 15)
veh.imprimirinformacoesV()
veh.acelerarV(15)
veh.desacelerarV(15)

bike = Bicicleta("Marca", "Rodas", "Modelo", 15, "Marchas", "Bagageiro")
bike.imprimirinformacoesB()

car = Carro("Marca", "Rodas", "Modelo", 15, "Potência do motor", "Total de portas")
car.imprimirinformacoesC()

motinho = Moto("Marca","Rodas","Modelo", 15,"Motor", "Partida elétrica")
motinho.imprimirinformacoesM()

auto = Automovel("Marca", "Rodas", "Modelo", 15, "Potência do motor")
auto.imprimirinformacoesA()
