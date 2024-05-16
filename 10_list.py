# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

numeros = [22, 15, 30, 17, 18, 299, 15, 27, 48, 31, 12, 68, 17, 18, 299, 15]

pares = sorted(set([valor for valor in numeros if valor % 2 == 0]))
impares = sorted(set([valor for valor in numeros if valor % 2 != 0]))

print('Pares: ', pares)
print('Impares', impares)