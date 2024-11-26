import json
import urllib.request
import urllib.parse
import boto3
from datetime import datetime

#Configurações do bucket
bucket = 'data-lake-heitor-ana'
storage = 'Raw'
source = 'TMDB'
file_type = 'JSON'

#Função para fazer o upload dos dados para o S3
def upload_para_s3(dados, bucket, storage, source, file_type, data_processamento, filename):
    path = f"{storage}/{source}/{file_type}/{data_processamento.year}/{data_processamento.month:02d}/{data_processamento.day:02d}/{filename}"
    
    s3 = boto3.client('s3') 

    try:
        s3.put_object(Bucket=bucket, Key=path, Body=json.dumps(dados, ensure_ascii=False, indent=4).encode('utf-8'))
        print(f"Arquivo {filename} enviado com sucesso para: {path}")
    except Exception as excecao:
        print(f"Erro ao enviar para o S3: {excecao}")

#Função handler para o Lambda
def lambda_handler(event, context):
    
    tmdb_api_key = "67c50927d4989b0a9353db649e01e4c9"

    apis = {
        "filmes_acao": {
            "url": "https://api.themoviedb.org/3/discover/movie",
            "params": {
                'api_key': tmdb_api_key,
                'language': 'pt-BR',
                'sort_by': 'popularity.desc',
                'with_genres': '28',
                'page': 1
            },
            "categoria": "FilmesAção",
            "filename": "filmes_acao.json"
        },
        "filmes_mais_avaliados": {
            "url": "https://api.themoviedb.org/3/movie/top_rated",
            "params": {
                'api_key': tmdb_api_key,
                'language': 'pt-BR',
                'with_genres': '28',
                'page': 1
            },
            "categoria": "FilmesMaisAvaliados",
            "filename": "filmes_mais_avaliados.json"
        },
        "filmes_populares": {
            "url": "https://api.themoviedb.org/3/movie/popular",
            "params": {
                'api_key': tmdb_api_key,
                'language': 'pt-BR',
                'with_genres': '28',
                'page': 1
            },
            "categoria": "FilmesPopulares",
            "filename": "filmes_populares.json"
        }
    }

    #Processamento de cada API
    for nome_api, config in apis.items():
        print(f"Processando API: {nome_api}")

        #Preparar a URL com os parâmetros
        url = f"{config['url']}?{urllib.parse.urlencode(config['params'])}"

        #Requisição API
        try:
            with urllib.request.urlopen(url) as response:
                if response.status != 200:
                    print(f"Erro ao fazer a requisição à API {nome_api}. Status: {response.status}")
                    continue
                dados_tmdb = json.loads(response.read().decode('utf-8'))
                print(f"Dados recebidos com sucesso da URL: {url}")
        except Exception as excecao:
            print(f"Erro ao fazer a requisição à API {nome_api}: {excecao}")
            continue

        data_processamento = datetime.now()

        upload_para_s3(dados_tmdb, bucket, storage, source, file_type, data_processamento, config["filename"])

    return {
        'statusCode': 200,
        'body': json.dumps('Processamento concluído com sucesso!')
    }
