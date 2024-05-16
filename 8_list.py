# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.


pessoas = [
    {"nome": "Carol", "idade": 20},
    {"nome": "Bob", "idade": 25},
    {"nome": "Alice", "idade": 30}
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)



# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Carol", "idade": 20}
# ]

# nova_lista = sorted(pessoas, key=lambda pessoas: pessoas['idade'])

# print(nova_lista)