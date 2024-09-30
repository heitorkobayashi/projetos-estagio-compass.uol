'''
Apresente a média de receita de bilheteria bruta dos principais filmes, considerando todos os atores.
Estamos falando aqui da média Gross.
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


soma_receita_total = 0.0
quantidade_filmes = 0


for dados in conteudo[1:]:  
    campos = limpar_dados(dados)  
    soma_receita_total += float(campos[5].strip())
    quantidade_filmes += 1
    

media_receita = soma_receita_total / quantidade_filmes


with open('etapa_2.txt', 'w') as resultado_arquivo:
    resultado_arquivo.write(f"Media de receita de bilheteria bruta dos principais filmes: {media_receita:.2f}")


print("Resultado salvo no arquivo 'etapa_2.txt'")