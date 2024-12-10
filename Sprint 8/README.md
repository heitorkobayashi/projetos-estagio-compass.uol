# **Instruções**

A oitava sprint teve como objetivo o aprofundamento em PySpark e Glue, exercitando também estes conceitos.

# **Certificados**

Essa sprint não teve cursos fora da Udemy, a não ser um curso opcional da AWS LATAM: _Tutoriais Técnicos - Analytics_

# **Exercícios**

#### Acesse as evidências dos exercícios através do seguinte link: **[Evidências dos exercícios](../Sprint%208/exercicios/evidencias/)**


Nesta sprint foram realizado dois exercícios, acesse as pastas respectivas clicando nos links abaixo: 

- **[Exercício TMDB:](../Sprint%208/exercicios/tmdb/)** Processo de extração de dados da API do TMDB
- **[Exercício Apache Spark:](../Sprint%208/exercicios/spark_batch/)** Spark Batch


## **Exercício TMDB**:

Este exercício consistia em criar um processo de extração de dados da API do TMDB. Para isso foi necessário criar uma conta no portal do TMDB para solicitar as chaves de acesso do uso da API.

**Acesse o código clicando aqui: [Código TMDB](../Sprint%208/exercicios/tmdb/tmdb_teste.ipynb)**

![tmdb](../Sprint%207/exercicios/evidencias/01_tmdb_teste.png)

- Acima, a imagem mostra o exemplo de código em Python para solicitação da API.

## **Exercício Spark Batch**:

Neste exercício foi utilizado um arquivo CSV para a criação de um Dataframe. Assim, foi possível testar comandos SQL. Para isso, foi gerado do zero um arquivo chamado `nomes_aleatorios.txt` que continha aproximadamente 10 milhões de nomes distintos.


| Etapa         | Descrição                                               | Link do código   |
| :------------ | :-------------------------------------------------------| :------------------|
|  Etapa 1      | Lista contendo 250 inteiros obtidos de forma aleatória  | [Código da Etapa 1](../Sprint%208/exercicios/spark_batch/1_geracao_massa_de_dados/etapa_1.py)  |
|  Etapa 2      | [Lista contendo o nome de 20 animais](../Sprint%208/exercicios/spark_batch/1_geracao_massa_de_dados/lista_animais.csv)  | [Código da Etapa 2](../Sprint%208/exercicios/spark_batch/1_geracao_massa_de_dados/etapa_2.py)  |
|  Etapa 3      | Gerar um dataset contendo aprox. 10 milhões de nome de pessoas  | [Código da Etapa 3](../Sprint%208/exercicios/spark_batch/1_geracao_massa_de_dados/etapa_3.py)   |


Abaixo, segue algumas evidencias dessas etapas:

![exercicio_script3](../Sprint%208/exercicios/evidencias/03_etapa3_script3.png)

- Script desenvolvido para realização da Etapa 3

![exercicio_nomes_aleatorios](../Sprint%208/exercicios/evidencias/05_nomes_aleatorios.png)

- Lista de nomes aleatórios gerado a partir do script anterior

Após essas primeiras etapas, com PySpark, foram resolvidos 9 exercícios que solicitavam a criação de um Dataframe e diversas manipulações, como:

- Adição de colunas
- Adição de valores de forma aleatória, evitando a utilização de funções de iteração
- Realização de queries utilizando SparkSQL
- Armazenamento de resultados em novos dataframes

**Acesse o código clicando aqui: [Código PySpark](../Sprint%208/exercicios/spark_batch/2_apache_spark/Sprint_8_Spark.ipynb)**

Nas imagens abaixo, podemos ver algum desses exercícios:

![exercicio_pyspark1](../Sprint%208/exercicios/evidencias/06_codigo_pyspark.png)

![exercicio_pyspark1](../Sprint%208/exercicios/evidencias/07_codigo_pyspark.png)

![exercicio_pyspark1](../Sprint%208/exercicios/evidencias/08_codigo_pyspark.png)

![exercicio_pyspark1](../Sprint%208/exercicios/evidencias/09_codigo_pyspark.png)


# **Desafio**

Acesse o desafio através do seguinte link: **[Desafio da Sprint](../Sprint%208/desafio/README.md)**

Acesse as evidências do desafio através do seguinte link: **[Evidências do desafio](/Sprint%208/evidencias/)**