with open('number.txt', 'r') as lista_numeros:
    conteudo_lista = lista_numeros.readlines()

conteudo_lista = map(lambda x: x.strip(), conteudo_lista)
conteudo_lista = map(int, conteudo_lista)
conteudo_lista = filter(lambda x: x % 2 == 0, conteudo_lista)
maiores_5 = sorted(conteudo_lista, reverse=True)[:5]
print(maiores_5)
print(sum(maiores_5))   
