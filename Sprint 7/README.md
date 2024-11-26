# **Instruções**

A sétima sprint teve como objetivo o aprofundamento em PySpark, utilização de APIs e exercitar conceitos de Glue e Lambda.

# **Certificados**

Essa sprint não teve cursos fora da Udemy.

# **Exercícios**

#### Acesse as evidências dos exercícios através do seguinte link: **[Evidências dos exercícios](../Sprint%207/exercicios/evidencias/)**


Nesta sprint foram realizado três laboratórios, acesse as pastas respectivas clicando nos links abaixo: 

- **[Exercício TMDB:](../Sprint%207/exercicios/tmdb/)** Processo de extração de dados da API do TMDB
- **[Exercício Apache Spark:](../Sprint%207/exercicios/pyspark/)** Contador de Palavras
- **[Lab AWS Glue:](../Sprint%207/exercicios/lab_glue/)** Processo de ETL utilizando AWS Glue

Abaixo, seguem algumas evidencias dos exercícios:

**Exercício TMDB**:

Este exercício consistia em criar um processo de extração de dados da API do TMDB. Para isso foi necessário criar uma conta no portal do TMDB para solicitar as chaves de acesso do uso da API.

Acesse o código clicando aqui: [Código TMDB](../Sprint%207/exercicios/tmdb/tmdb_teste.ipynb)

![tmdb](../Sprint%207/exercicios/evidencias/01_tmdb_teste.png)

- Acima, a imagem mostra o exemplo de código em Python para solicitação da API.

**Exercício Apache Spark**:

Neste exercício foi desenvolvido um processamento com Spark, por meio de um container Docker, um código capaz de contar a quantidade de ocorrências de cada palavra no arquivo README.md do repositório aqui do GitHub.

Acesse o código clicando aqui: [Código Spark](../Sprint%207/exercicios/pyspark/script_spark.py)

Na imagem abaixo podemos ver a imagem do `jupyter/all-spark-notebook` construida.

![spark_imagem](../Sprint%207/exercicios/evidencias/01_spark_imagem.png)

Após realizado o mapeamento da porta do serviço parara uma porta local da máquina, podemos ver o código em execução através do navegador.

![spark_execucao](../Sprint%207/exercicios/evidencias/04_spark_contador_palavras.png)


**Lab AWS Glue**:

Neste laboratório foi realizado a construção de um processo de ETL utilizando AWS Glue. 

Acesse o código clicando aqui: [Código Glue](../Sprint%207/exercicios/lab_glue/lab_glue.ipynb)

Acesse o arquivo .CSV, resultado do Athena, clicando aqui: [Arquivo CSV](../Sprint%207/exercicios/lab_glue/crawler_athena.csv)

Esse exercício foi separado em x etapas:

- 1. Preparação dos dados de origem
- 2. Criação da IAM Role para os jobs do AWS Glue
- 3. Configuração da conta para utilizar o Glue
- 4. Configuração de permisões no AWS Lake Formation
- 5. Criação de um novo Job no Glue: exercícios
- 6. Criação do crawler

Abaixo, seguem algumas evidencias da realização deste lab:

![pasta_labglue](../Sprint%207/exercicios/evidencias/02_glue_pasta_labglue.png)

- Pasta `lab-glue`

![frequencia_labglue](../Sprint%207/exercicios/evidencias/03_glue_pasta_frequencia_01.png)

- Pasta `frequencia_registro_nomes_eua`, após realização do job.

![glue_schemas](../Sprint%207/exercicios/evidencias/06_glue_schemas.png)

- Log do schema solicitado

![glue_logs](../Sprint%207/exercicios/evidencias/07_glue_logs_registros.png)

- Log dos jobs solicitados

![glue_crawler_athena](../Sprint%207/exercicios/evidencias/09_glue_crawler_athena.png)

- Query final no Athena

# **Desafio**

Acesse o desafio através do seguinte link: **[Desafio da Sprint](../Sprint%207/desafio/README.md)**

Acesse as evidências do desafio através do seguinte link: **[Evidências do desafio](../Sprint%207/evidencias/)**