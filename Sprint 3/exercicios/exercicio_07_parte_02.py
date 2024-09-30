'''
Dada a seguinte lista:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Faça um programa que gere uma nova lista contendo apenas números ímpares.
'''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista = []

for item in a:
    if item % 2 != 0:
        lista.append(item) #append adiciona os itens na lista
        
print(lista)
