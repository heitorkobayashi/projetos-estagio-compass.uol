'''
Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento
e uma função como segundo argumento.
Esta função aplica a função recebida para cada elemento da lista
recebida e retorna o resultado em uma nova lista.

Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e com uma função que potência de 2 para cada elemento.
'''

def my_map(lista, f):
    resultado = []
    for item in lista:
        resultado.append(f(item)) #lembrar do append pra adicionar 
    return resultado
    
def lista_potencia_2(x):
    return x ** 2
    
entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = my_map(entrada, lista_potencia_2)

print(resultado)
