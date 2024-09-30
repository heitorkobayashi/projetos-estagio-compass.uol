'''
Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.
Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
'''

lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in lista:
    if palavra == palavra[::-1]: #compara com o inverso das palavras 
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")
