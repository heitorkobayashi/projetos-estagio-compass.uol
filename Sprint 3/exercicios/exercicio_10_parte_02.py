'''
Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados.
Utilize a lista a seguir para testar sua função.
['abc', 'abc', 'abc', '123', 'abc', '123', '123']
'''

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def func_lista(lista):
    nova_lista = list(set(lista)) #set cria um conjunto, eliminando dados duplicados
    return nova_lista

print(func_lista(lista))
