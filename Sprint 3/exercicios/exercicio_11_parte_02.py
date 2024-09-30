'''
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
'''

import json

arquivo = 'person.json'

with open(arquivo, 'r') as arq: 
    dados = json.load(arq) #colocando indent=x formata a saida de forma mais fácil de ler

print(dados)
