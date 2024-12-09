import random

numeros = [random.randint(1, 10000) for _ in range(250)]
numeros.reverse()
print(numeros)
