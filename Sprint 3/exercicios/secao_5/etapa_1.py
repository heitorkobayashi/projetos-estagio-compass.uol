'''
Apresente o ator/atriz com maior número de filmes e a respectiva quantidade. 
A quantidade de filmes encontra-se na coluna Number of movies do arquivo.
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


maior_numero_filmes = int('-1')
ator = ''

for dados in conteudo[1:]:  
    campos = limpar_dados(dados)  
    numero_filmes = int(campos[2].strip())
    
    if numero_filmes > maior_numero_filmes:
        maior_numero_filmes = numero_filmes
        ator = campos[0].strip()


with open('etapa_1.txt', 'w') as resultado_arquivo:
    resultado_arquivo.write(f"{ator} possui o maior numero de filmes: {maior_numero_filmes} filmes.")

print("Resultado salvo no arquivo 'etapa_1.txt'")
