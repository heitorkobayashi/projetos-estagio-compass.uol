'''
Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:

Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
'''

import random

random_list = random.sample(range(500), 50)


mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0

#mediana
sorted_list = sorted(random_list)
numero = len(sorted_list)
if numero % 2 == 0:
    mediana = (sorted_list[numero // 2 - 1] + sorted_list[numero // 2]) / 2
else:
    mediana = sorted_list[numero // 2]
    
#media
media = sum(random_list) / len(random_list)

#minimo
valor_minimo = min(random_list)

#maximo 
valor_maximo = max(random_list)

print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")
