estudante = input("Voce e estudante?")
idade = int(input('Digite sua idade: '))
preco = 100

if estudante == 'sim':
    preco = preco - (preco * 0.10)
    print(preco)
else:
    print(preco)

if idade <= 12:
    preco = preco * 0.50
    print(preco)
elif idade >= 60:
    preco = preco - (preco * 0.30)
    print(preco)
