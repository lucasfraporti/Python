produtos = ['calça', 'bota', 'água']
valor = ['R$100,00', 'R$20,00', 'R$5,00']
quantidade_produtos = [6, 10, 18]

def remover_produtos():
    if produto_remover in produtos:
        produtos.remove(produto_remover)
        valor.pop(produto_remover.index(produto_remover))
        quantidade_produtos.pop(produto_remover.index(produto_remover))
    else:
        return 'O produto não está na lista de produtos'
    return str(produtos) + '\n' + str(valor) + '\n' + str(quantidade_produtos)

def imprimir_produto():
    if produto_ler_index <= (len(produtos)-1):
        return str(produtos[produto_ler_index]) + '\n' + str(valor[produto_ler_index]) + '\n' + str(quantidade_produtos[produto_ler_index])
    else:
        return 'O produto não está na lista de produtos' 

while True:
    menu = int(input('1 - Impressão de um produto específico\n2 - Exclusão de um produto específico\nEscolha uma opção: '))

    if menu == 1:
        print(produtos)
        produto_ler_index = int(input('Digite a posição do produto que você quer imprimir: '))
        print(imprimir_produto())

    elif menu == 2:
        produto_remover = input('Digite o produto que você quer remover: ')
        print(remover_produtos())
