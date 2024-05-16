# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades = [22, 15, 30, 17, 18]

nova_lista = [item for item in idades if item>=18]

print(nova_lista)
