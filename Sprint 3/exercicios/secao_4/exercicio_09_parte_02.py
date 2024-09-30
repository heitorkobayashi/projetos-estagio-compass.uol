'''
Dada as listas a seguir:
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".
'''
#Você deve Utilizar a função enumerate().

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, (primeirosNomes, sobreNomes, idades) in enumerate(zip(primeirosNomes, sobreNomes, idades), start=0):
    print(f"{indice} - {primeirosNomes} {sobreNomes} está com {idades} anos")
    