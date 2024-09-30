'''
A coluna #1 Movie contém o filme de maior bilheteria em que o ator atuou.
Realize a contagem de aparições destes filmes no dataset, listando-os ordenados pela quantidade
de vezes em que estão presentes. Considere a ordem decrescente e, em segundo nível, o nome do filme.

Ao escrever no arquivo, considere o padrão de saída:
(sequência) - O filme (nome do filme) aparece (quantidade) de vez(es) no dataset, adicionando um resultado a cada linha
'''

arquivo_csv = 'actors.csv'

# Função para limpar os dados
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


filme = {}


for dados in conteudo[1:]:  
    campos = limpar_dados(dados)  
    nome_do_filme = campos[4].strip()


    if nome_do_filme in filme:
        filme[nome_do_filme] += 1
    else:
        filme[nome_do_filme] = 1


lista_filmes = sorted(filme.items(), key=lambda x: x[1], reverse=True)


with open('etapa_4.txt', 'w') as resultado_arquivo:
    for nome, quantidade in lista_filmes:
        resultado_arquivo.write(f"O filme {nome} aparece {quantidade} vez(es) no dataset.\n")

    
print("Resultado salvo no arquivo 'etapa_4.txt'")
