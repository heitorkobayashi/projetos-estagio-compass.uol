# **Sprint 9: Desafio**

## **1. Objetivos**

Este desafio teve como objetivo a modelagem de dados e processamento da camada Refined. Para isso, houve a manipulação do Apache Spark, utilizando um job através do AWS Glue para integrar os dados existentes na camada Trusted Zone com destino em uma camada intermediária, a camada Staging. A partir desses dados, foi definida a modelagem dimensional e um novo processamento para a criação da camada Refined.  

Clique nos seguintes links para acessar os respectivos códigos e arquivos:

- [Código do Job da camada Staging](../desafio/entrega_4/job_camada_staging.py)
- [Código do Job da camada Refined](../desafio/entrega_4/job_camada_refined.py)
- [Diagrama da modelagem dimensional](../desafio/entrega_4/modelo_dimensional.png)


## **2. Definição de Tema - Perguntas a serem respondidas**

Agora com acesso às APIs foi possível visualizar certos dados que não tínhamos acesso anteriomente. O meu desafio abordará a **Análise da Relação entre Orçamento e Qualidade em Filmes de Ação da década de 2000 a 2010**. Dessa forma, as perguntas motivadoras a serem respondidas na minha pesquisa são:

- O orçamento de produção está diretamente relacionado às notas de avaliação dos filmes de ação?

- Filmes de baixo orçamento podem alcançar qualidade semelhante a filmes de alto orçamento?

Tendo em vista que a década de 2000 a 2010 foi um perído de transição no cinema, muito marcado pela popularização do uso de tecnologias como CGI e das expansões de certas franquias, podemos nos atentar a algumas questões, como:

- Filmes com orçamento elevado tiveram maior sucesso comercial entre 2000 e 2010?

- Existe uma correlação entre o orçamento de um filme de ação e sua nota média durante o período?

- O surgimento de tecnologias, como CIG, na década de 2000 impactou a relação entre orçamento e qualidade dos filmes de ação?

- Como os filmes de ação da década de 2000 a 2010 se diferem em termos de orçamento e qualidade em comparação a décadas anteriores ou posteriores?

## **3. Camada Staging**

O primeiro passo realizado foi a criação de um database: 

![imagem_db](../evidencias/16_database.png)

## **4. Camada Refined**

Para fazer a integração de dados da camada Raw para a camada Trusted, foi realizado dois códigos distintos, um para o arquivo CSV e outro para os arquivos em JSON. Abaixo, é possível ver o código do Job para o arquivo CSV.

![imagem_job_csv](../evidencias/04_job_csv.png)

O script processa os arquivos CSV da camada Raw, transforma os dados em Parquet e os organiza na camada Trusted do Data Lake. Para isso, primeiramente, foram definidos os parâmetros de entrada:

![imagem_job_details_1](../evidencias/15_job_details_csv.png)

Após algumas tentativas sem sucesso, para a leitura dos dados, foi utilizado o `delimiter="|"`, pois é nessa estrutura que o arquivo CSV se encontrava. Isso foi percebido pois algumas tentativas foram bem sucedidas, mas infelizmente, ao realizar as consultas no Athena, os dados estavam todos bagunçados. Abaixo, podemos ver algumas das tentativas realizadas.

![imagem_job_runnings](../evidencias/05_job_csv_runs.png)

Na próxima imagem, podemos ver o resultado do script, a conversão para Parquet foi bem sucedida. 

![imagem_job_parquet](../evidencias/06_parquet_csv.png)


Nesse script eu não me preocupei em retirar colunas que não seriam utilizadas, o objetivo foi apenas particionar e fazer a conversão para Parquet, mantendo todos os dados obtidos.

### **4.2. Job JSON**

Agora, para fazer a integração dos dados obtidos da coleta da API, o passo a passo foi basicamente o mesmo.

![imagem_job_json](../evidencias/08_job_json.png)

Este script é bem similar ao script do CSV, mas com algumas diferenças:

-  Utilização de funções auxiliares, como `lit` para criar colunas com valores constantes, `col` para facilitar a manipulação de colunas do DataFrame, `input_file_name` que permite acessar o nome do arquivo de entrada e `datetime` para obter a data atual e adicionar metadados ao DataFrame. 
- Leitura dos arquivos JSON no caminho especificado utilizando `option("multiline", "true")`, pois os arquivos JSON possuem múltiplas linhas por registro.
- Particionamento por data, com filtragem para os nomes ficarem da maneira correta.

A seguir, podemos ver as tentativas de execução do job e o particionamento no S3.

![imagem_run_json](../evidencias/09_job_json_runs.png)

![imagem_parquet_json](../evidencias/10_parquet_json.png)

Dessa forma, realizado os Jobs, o bucket no S3 ficou assim:

![imagem_pasta_trusted](../evidencias/12_pasta_trusted.png)



### **5. Crawlers**

Os crawlers são ferramentas automatizadas com o objetivo de explorar os dados armazenados. No nosso caso, esses dados estão no S3. Ele é capaz de realizar automaticamente a estrutura (esquema) desses dados e criar tabelas no Glue Data Catalog.

Neste desafio, optei pela criação de dois crawlers, um para os dados extraídos do CSV e outro para os dados extraídos dos arquivos JSON.

![imagem_crawler](../evidencias/13_crawlers.png)

A criação desses crawlers são bem simples, basicamente bastou informar corretamente o caminho do S3 e executar. Podemos ver o resultado no Athena:

![imagem_athena](../evidencias/14_consulta_athena.png)

Na query acima, foi realizado uma consulta com join entre as tabelas para verificar se estava tudo correto. E essa foi a última estapa deste desafio.
