texto = input("Digite um texto")
tamanho_texto = len(texto)
mais_de_cinco = None

if tamanho_texto > 5:
    mais_de_cinco = True
else:
    mais_de_cinco = False

print("o texto é", texto, "O boolean é", mais_de_cinco)