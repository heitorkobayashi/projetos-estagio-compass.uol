import json
import requests
import boto3
from datetime import datetime, timezone


bucket = 'data-lake-heitor-ana'
storage = 'Raw'
source = 'TMDB'
file_type = 'JSON'


def upload_para_s3(dados, bucket, storage, source, file_type, data_processamento, endpoint):

    endpoint = endpoint.replace("/", "-")

    path = f"{storage}/{source}/{file_type}/{data_processamento.year}/{data_processamento.month:02d}/{data_processamento.day:02d}/{endpoint}.json"
    
    s3 = boto3.client('s3')

    try:
        s3.put_object(Bucket=bucket, Key=path, Body=json.dumps(dados, ensure_ascii=False, indent=4).encode('utf-8'))
        print(f"Arquivo enviado com sucesso para: {path}")
    except Exception as excecao:
        print(f"Erro ao enviar para o S3: {excecao}")


def buscar_ids_filmes(api_key, endpoint, parametros, max_paginas=20, genero_id=28):

    movie_ids = []

    for page in range(1, max_paginas + 1):

        parametros.update({'api_key': api_key, 'page': page})
        url = f"https://api.themoviedb.org/3/{endpoint}"

        try:
            resposta = requests.get(url, params=parametros)
            resposta.raise_for_status()
            data = resposta.json()
            
            ids_endpoint = [
                filme['id']
                for filme in data.get('results', [])
                if genero_id in filme.get('genre_ids', [])
            ]
            movie_ids.extend(ids_endpoint)
        except requests.exceptions.RequestException as excecao:
            print(f"Erro na página {page} do endpoint {endpoint}: {excecao}")
    
    return list(set(movie_ids))


def buscar_detalhes_filmes(api_key, movie_ids):

    filmes_detalhes = []

    for movie_id in movie_ids:

        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        parametros = {'api_key': api_key, 'language': 'pt-BR'}

        try:
            response = requests.get(url, params=parametros)
            response.raise_for_status()
            data = response.json()
            filmes_detalhes.append(data)
        except requests.exceptions.RequestException as excecao:
            print(f"Erro ao buscar detalhes do filme {movie_id}: {excecao}")
    
    return filmes_detalhes


def lambda_handler(event, context):

    api_key = '67c50927d4989b0a9353db649e01e4c9'
    endpoints = ['movie/popular', 'movie/top_rated', 'movie/now_playing']
    parametros = {}
    genero_id = 28
    
    for endpoint in endpoints:

        print(f"Buscando IDs de filmes do {endpoint}...")
        movie_ids = buscar_ids_filmes(api_key, endpoint, parametros, max_paginas=50, genero_id=genero_id)

        print(f"Total de IDs coletados do '{endpoint}' (gênero ação): {len(movie_ids)}")
        
        print(f"Buscando detalhes dos filmes do {endpoint}...")
        filmes_detalhes = buscar_detalhes_filmes(api_key, movie_ids)

        print(f"Total de filmes com detalhes coletados do '{endpoint}': {len(filmes_detalhes)}")
        
        data_processamento = datetime.now()

        upload_para_s3(filmes_detalhes, bucket, storage, source, file_type, data_processamento, endpoint)

    return {
        "statusCode": 200,
        "body": json.dumps(f"Concluído. Dados enviados para o bucket {bucket}.")
    }
