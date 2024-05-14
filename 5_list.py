# 5.Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista_de_compras = ["maçã", "banana", "cereja"]

precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

calculo = sum(precos[item] for item in lista_de_compras)

print(f"Preço total: ", calculo)



