'''
Escreva um programa que lê o conteúdo do arquivo texto
arquivo_texto.txt e imprime o seu conteúdo.
'''

with open("arquivo_texto.txt", "r") as arquivo_texto:
    conteudo = arquivo_texto.read()
print(conteudo)
