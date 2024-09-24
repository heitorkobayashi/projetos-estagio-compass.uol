'''
Escreva um código Python que use a função range() para adicionar três números
em uma lista(Esta lista deve chamar-se 'números') e verificar se esses três números
são pares ou ímpares. Para cada número, imprima como saída
Par: ou Ímpar: e o número correspondente (um linha para cada número lido).

Importante: Aplique a função range() em seu código.

Exemplos de saída:

Par: 2
Ímpar: 3
'''
#criação da lista vazia
numeros = []

#loop for num in range(3): Gera três números, de 0 a 2.
for num in range (3):
    numeros.append(num) #Adiciona cada número à lista numeros usando append().
    if num % 2 == 0: #Verifica se o número é par ou ímpar: Usa if num % 2 == 0 para verificar se o número é divisível por 2.
        print("Par:", num)
    else:
        print("Ímpar:", num)
    