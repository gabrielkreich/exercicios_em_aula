# pedir para o usuario para inserir um codigo do produto
# usar o match case para encontrar o produto pelo código

cod_produtos = int(input("Digite o código do produto: "))

match cod_produtos:
    case 1:
        print("Eletronicos")
    case 2:
        print("Roupas")
    case 3:
        print("Alimentos")
    case 4:
        print("Livros")
    case 5:
        print("Brinquedos")
    case _:
        print("Código inválido")

