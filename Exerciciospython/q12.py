# numero1 = input("Escolha o primeiro numero: ")
# numero2 = input("Escolha o segundo numero: ")
# numero3 = input("Escolha o terceiro numero: ")
#
# lista = [numero1, numero2, numero3]
#
# print(lista)

lista = []

# utilizar FOR para repetição
for i in range(3):
    numero = float(input(f"Digite o {i+1}º número: "))
    lista.append(numero)

#SORT para ordenar
lista.sort()

print(lista)
