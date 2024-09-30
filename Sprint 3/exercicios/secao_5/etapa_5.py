'''
Apresente a lista dos atores ordenada pela receita bruta de bilheteria de seus filmes (coluna Total Gross), em ordem decrescente
Ao escrever no arquivo, considere o padrão:
(nome do ator) - (receita total bruta), adicionando um resultado a cada linha
'''


arquivo_csv = 'actors.csv'


def limpar_dados(dados):
    colunas = [] 
    coluna_atual = ''
    aspas = False  

    for caractere in dados:
        if caractere == '"':  
            aspas = not aspas  
        elif caractere == ',' and not aspas:  
            colunas.append(coluna_atual.strip())  
            coluna_atual = '' 
        else:
            coluna_atual += caractere  

    colunas.append(coluna_atual.strip())
    
    return colunas 


with open(arquivo_csv, 'r') as arquivo:
    conteudo = arquivo.readlines()  


ator_receita = {}
receita_bruta = 0.0

for dados in conteudo[1:]:  
    campos = limpar_dados(dados)
    ator = campos[0].strip()
    receita_bruta = float(campos[5].strip())

    if ator in ator_receita:
        ator_receita[ator] += receita_bruta
    else:
        ator_receita[ator] = receita_bruta


lista_atores = sorted(ator_receita.items(), key=lambda x: x[1], reverse=True)


with open('etapa_5.txt', 'w') as resultado_arquivo:
    for nome, receita in lista_atores:
        resultado_arquivo.write(f"{nome} - {receita}.\n")

    
print("Resultado salvo no arquivo 'etapa_5.txt'")