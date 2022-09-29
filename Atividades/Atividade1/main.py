produtos = ["calça", "bota", "água"]
valor = ["R$100,00", "R$20,00", "R$5,00"]
quantidade_produtos = [6, 10, 18]

def imprimir_produto(index):
    if(index <= (len(produtos)-1)):
        return f"{str(produtos[index])}\n{str(valor[index])}\n{str(quantidade_produtos[index])}"
    else:
        return "O produto não está na lista de produtos" 

def remover_produtos(produto_remover):
    if(produto_remover in produtos):
        i = produtos.index(produto_remover)
        produtos.remove(produto_remover)
        valor.pop(i)
        quantidade_produtos.pop(i)
    else:
        return "O produto não está na lista de produtos"
    return f"Produtos restantes: {str(produtos)}\nValores dos produtos: {str(valor)}\nTotal em estoque: {str(quantidade_produtos)}"

if __name__ == '__main__':
    while True:
        menu = int(input("1 - Impressão de um produto específico através do index.\n2 - Exclusão de um produto específico.\nEscolha uma opção: "))

        if(menu == 1):
            for produtinhos in produtos:
                i = produtos.index(produtinhos)
                print(f"[{i}] - {produtinhos}")
            index = int(input("Digite a posição do produto que você quer imprimir: "))
            print(imprimir_produto(index))

        elif(menu == 2):
            produto_remover = input("Digite o produto que você quer remover: ")
            print(remover_produtos(produto_remover))

        else:
            print("A opção que você selecionou é inválida.")