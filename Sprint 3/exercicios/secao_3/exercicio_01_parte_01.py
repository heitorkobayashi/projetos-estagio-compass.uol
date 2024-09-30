'''
Desenvolva um código em Python que crie variáveis para armazenar
o nome e a idade de uma pessoa, juntamente com seus valores correspondentes.
Como saída, imprima o ano em que a pessoa completará 100 anos de idade.
'''

#importação biblioteca datetime para trabalhar com data e hora atuais
from datetime import datetime

nome = 'alana'
idade = 25

current_year = datetime.now().year #datetime.now() retorna a data e hora atuais. Com .year extrai apenas o ano atual (2024)

idade_100 = current_year + (100 - idade)

print(idade_100)