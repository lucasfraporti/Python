mp = int(input("Digite o multiplicando: "))
mi = int(input("Digite o multiplicador inicial: "))
mf = int(input("Digite o multiplicador final: "))
print(f"Multiplicador inicial: {mi}\nMultiplicador final: {mf}\nTabuada do {mp}")

def Tabuada(mp, mi, mf):
    for i in range(mi, mf+1):
        print(f"{mp}x{i} = {mp*i}")

Tabuada(mp, mi, mf)