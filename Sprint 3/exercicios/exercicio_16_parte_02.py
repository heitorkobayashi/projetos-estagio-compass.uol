'''
Escreva uma função que recebe uma string de números separados por vírgula
e retorne a soma de todos eles. Depois imprima a soma dos valores.

A string deve ter valor  "1,3,4,6,10,76"
'''

def soma (str_numeros):
    lista_numeros = str_numeros.split(",")
    lista_int = [int(numero) for numero in lista_numeros] # converter a lista
    soma = sum(lista_int)
    return soma

numeros = "1,3,4,6,10,76"

resultado = soma(numeros)
print(resultado)
