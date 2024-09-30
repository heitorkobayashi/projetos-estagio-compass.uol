'''
Apresente ator/atriz com a maior média de bilheteria bruta por filme do conjunto de dados.
Considere a coluna Average per Movie para fins de cálculo
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


maior_bilheteria = float('-inf')
ator = ''


for dados in conteudo[1:]:  
    campos = limpar_dados(dados)  
    bilheteria = float(campos[3].strip())

    if bilheteria > maior_bilheteria:
        maior_bilheteria = bilheteria
        ator = campos[0].strip() 
    

with open('etapa_3.txt', 'w') as resultado_arquivo:
    resultado_arquivo.write(f"{ator} possui a maior media de bilheteria bruta, no valor de {maior_bilheteria:.2f}.")


print("Resultado salvo no arquivo 'etapa_3.txt'")