#numero = int(input("Escolha um numero:"))
#if numero % 2 == 0:
#    print("este numero e par")
#else:
#    print("este numero e impar")

numero = int(input("Digite um número inteiro: "))
e_par = "par" if numero%2==0 else "impar"

print(f"O número é {numero} e o boolean é {e_par}")