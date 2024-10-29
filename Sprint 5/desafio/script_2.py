import pandas as pd
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Leitura do arquivo no bucket
sessao = boto3.Session(profile_name='heitorkobayashi')
s3_client = sessao.client('s3')
bucket_nome = 'meu-bucket-desafio-2'
nome_arquivo_csv_s3 = 'lancamentos_comerciais_por_distribuidoras.csv'

try:
    obj = s3_client.get_object(Bucket=bucket_nome, Key=nome_arquivo_csv_s3)
    df = pd.read_csv(obj['Body'], delimiter=';')
except Exception as excessao:
    print(f"Erro ao ler o arquivo CSV: {excessao}")
    exit(1)

# 4.1 Filtrando com operadores lógicos: Obras de ficção no Brasil com público superior a 1000
df_filtrado = df[(df['TIPO_OBRA'] == 'FICÇÃO') & (df['PAIS_OBRA'] == 'BRASIL') & (df['PUBLICO_TOTAL'] > 1000)]

# 4.2 Duas funções de agregação: 
# Contagem de obras por país
contagem_por_pais = df.groupby('PAIS_OBRA').size().reset_index(name='Contagem')

# Público total por tipo de obra
publico_por_tipo = df.groupby('TIPO_OBRA')['PUBLICO_TOTAL'].sum().reset_index(name='Publico_Total')

# 4.3 Uma função condicional: Obras que têm baixo e alto público
df['PUBLICO_NIVEL'] = df['PUBLICO_TOTAL'].apply(lambda x: 'Alto' if x > 500 else 'Baixo')

# 4.4 Uma função de conversão: Remoção do "R$", dos espaços e conversão para float
df = df[df['RENDA_TOTAL'].str.strip() != '']
df['RENDA_TOTAL'] = df['RENDA_TOTAL'].replace(r'[R\$]', '', regex=True) 
df['RENDA_TOTAL'] = df['RENDA_TOTAL'].str.replace('.', '', regex=True)
df['RENDA_TOTAL'] = df['RENDA_TOTAL'].str.replace(',', '.')

# 4.5 Uma função de data: Extração do mês de lançamento dos filmes
df['DATA_LANCAMENTO_OBRA'] = pd.to_datetime(df['DATA_LANCAMENTO_OBRA'], format='%d/%m/%Y')
df['MES_LANCAMENTO'] = df['DATA_LANCAMENTO_OBRA'].dt.month

# 4.6 Uma função de string: Extração do nome principal da distribuidora
df['NOME_DISTRIBUIDORA'] = df['RAZAO_SOCIAL_DISTRIBUIDORA'].str.split().str[0]

# Concatenando todas as manipulações em um único df para exportar em .csv
df_resultado = pd.concat([df_filtrado[['TITULO_ORIGINAL', 'TIPO_OBRA', 'PAIS_OBRA', 'PUBLICO_TOTAL']],
                           contagem_por_pais,
                           publico_por_tipo,
                           df[['TITULO_ORIGINAL', 'PUBLICO_TOTAL', 'PUBLICO_NIVEL']],
                           df[['TITULO_ORIGINAL', 'RENDA_TOTAL']],
                           df[['TITULO_ORIGINAL', 'DATA_LANCAMENTO_OBRA', 'MES_LANCAMENTO']],
                           df[['RAZAO_SOCIAL_DISTRIBUIDORA', 'NOME_DISTRIBUIDORA']]
                          ], axis=1)

nome_arquivo_csv = 'resultado_manipulacoes.csv'
df_resultado.to_csv(nome_arquivo_csv, index=False)

# Enviando o arquivo csv para o bucket
try:
    s3_client.upload_file(nome_arquivo_csv, bucket_nome, nome_arquivo_csv)
    print(f"Arquivo '{nome_arquivo_csv}' enviado para o bucket '{bucket_nome}' com sucesso!")
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo_csv}' não foi encontrado.")
except NoCredentialsError:
    print("Credenciais não encontradas. Verifique suas configurações de autenticação.")
except PartialCredentialsError:
    print("Credenciais incompletas fornecidas. Verifique suas configurações.")
except Exception as excessao:
    print(f"Ocorreu um erro: {excessao}")
