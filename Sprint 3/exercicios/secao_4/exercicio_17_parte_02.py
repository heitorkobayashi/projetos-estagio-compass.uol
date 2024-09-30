'''
Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas:
a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
'''

def listas(lista):
    tamanho = len(lista) // 3
    lista_1 = lista[:tamanho]
    lista_2 = lista[tamanho:tamanho*2]
    lista_3 = lista[tamanho*2:]
    return lista_1, lista_2, lista_3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

partes = listas(lista)

print(f"{partes[0]} {partes[1]} {partes[2]}")
