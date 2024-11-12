import boto3
from datetime import datetime

#Configurações do bucket
bucket = 'data-lake-heitor-ana'
storage = 'Raw'
source = 'Local'
file = 'CSV'

#Caminhos locais dos arquivos
local_path = {
    'movies': '/desafio/entrega_1/movies.csv',
    'series': '/desafio/entrega_1/series.csv'
}

#Subdiretórios no S3
categoria_paths = {
    'movies': 'Movies',
    'series': 'Series'
}

#Data atual
hoje = datetime.now()
data_path = f"{hoje.year}/{hoje.month:02}/{hoje.day:02}"
aws_access_key_id = 'ASIA3CMCCG5U2AENIJ5S'
aws_secret_access_key = 'ZcTRkbmDhSYj4iC6spqnI+W3BgrBtz2o/Bpv7m18'
aws_session_token = 'IQoJb3JpZ2luX2VjEPL//////////wEaCXVzLWVhc3QtMSJHMEUCIQDYNeyUWJXbU6c8/EIByPf/Wp4hiV5ZJPKUb1h192MEQwIgYfYmstO/18hyjpu7QNwo3MK7nMqa3r6N28LKz+JA280qmQMIexAAGgw3NjEwMTg4NTczMjEiDK7a8ZkQ9azfymsYKSr2Auw3HltP3HoUnvpWNy1WpnAcAI9PzRt8gZjF3Pcl6loolkb67Am6hZxv6IHcYVT8w5N9PdmpVbyRGzRAeR+2tPIdw5jNLjQDDiildteLC4ww5dVnydIeRLWgMCYC3u1bhnAnTGp3MB2EiaGGfpjgr/e1Dba3OcLWqqslWL4f6MLvGReKh6fgiRb9pubiMBvT/adkcOVFwN4GrBRValA8bG1fcaZbz7PDG0MT2AXMqXF7k53qHfsAAq3jHxhp9bRcjP1d+6XRW6MCjxsf9t35evkVNMa0+HmKIzH33mxU+El+VrET4CQW+JzGMEY0k/OeyfKoJeKF1AERc8M7aKSqx8e4T/3zmF+JKdSgEtX2GPi7E0Hm4KzIqT0tvkvQ1aX/zrRMZ8CFHCyT3dDK/NDEx/5sPBwbgKjP3z+5yTQHEpxV6Dqa+RjjYnYb3MdOgnK493IY0d1TJdHrmPbP7OyBiEYq0B68+8/xDkj4MTRINupUjszdQxrBMKi1vrkGOqYBRsGKfVUnLziWSX6mcZfGU7KAkjI0/UXxwwpi7NTxQfSuiTQnZZOKpwT4jRNDgbaZP3cItRITEDH/pWV3maJhfuxXeCh8q06XNRWCnceBdsWR4xOB/rfyLhk02w95FiQ5xUUVfRA9nFLMPLbPQfj1u6r0LW1DvzrZh31ibh1ij4eI4uVXcRTJu4+mVjJhl5UWvXms6cVDqjdPJEwP40/5xu+bDn9xiw=='

#Função de upload dos arquivos para o S3
def upload_arquivos(s3_client, file_path, s3_path):
    try:
        s3_client.upload_file(file_path, bucket, s3_path)
        print(f'Upload de {file_path} para {s3_path} realizada com sucesso.')
    except Exception as e:
        print(f'Falha no upload de {file_path}: {str(e)}.')

#Função principal para upload dos arquivos csv
def main():

    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token
    )
    
    #Upload dos arquivos
    for file_key, file_path in local_path.items():
        s3_path = f"{storage}/{source}/{file}/{categoria_paths[file_key]}/{data_path}/{file_key}.csv"
        upload_arquivos(s3_client, file_path, s3_path)

#Executar o script
if __name__ == "__main__":
    main()
