import names
import random
import time


random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000


aux = []
for i in range(qtd_nomes_unicos):
    nome = names.get_full_name()
    if nome not in aux:
        aux.append(nome)


print(f"Gerando {qtd_nomes_aleatorios} nomes")


with open("nomes_aleatorios.txt", "w") as arquivo:
    for i in range(qtd_nomes_aleatorios):
        arquivo.write(random.choice(aux) + "\n")


print("\nArquivo 'nomes_aleatorios.txt' gerado!")
