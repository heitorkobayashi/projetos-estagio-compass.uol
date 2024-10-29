import boto3

sessao = boto3.Session(profile_name='heitorkobayashi')
s3 = sessao.client('s3')

bucket_nome = 'meu-bucket-desafio-2'
arquivo_local = r'J:\Compass.Uol\Estágio 2024\#Sprints_heitordocs\Sprint 5\Desafio\lancamentos_comerciais_por_distribuidoras.csv'
arquivo_s3 = 'lancamentos_comerciais_por_distribuidoras.csv'

try:
    s3.upload_file(arquivo_local, bucket_nome, arquivo_s3)
    print(f"Arquivo '{arquivo_local}' enviado com sucesso para o bucket '{bucket_nome}'!")
except Exception as excecao:
    print(f"Erro ao enviar o arquivo: {excecao}")
