# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com","user@example.com", "admin@example.com","admin@example.com", "user@example.com", "manager@example.com"]

emais_unicos = list(set(emails))

print(emais_unicos)