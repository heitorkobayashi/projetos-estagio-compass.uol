'''
Escreva um código Python para imprimir todos os números primos entre 1 até 100.
Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.

Importante: Aplique a função range().
'''

for numero in range (2, 100):
    numero_primo = True                
    for divisao in range(2, numero): #verifica se o numero pode ser dividido por algum número menor que ele
        if numero % divisao == 0:
            numero_primo = False    #se puder ser dividido, variável é alterada pra false
            break                   #interrompe o loop
    if numero_primo:
        print(numero)