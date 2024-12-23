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

A camada _Staging_ é uma camada intermediária onde os dados pré processados são armazenados de forma temporária. Ela foi de extrema importância, pois serviu como um buffer para preparar esses dados antes de realizar o dimensionamento, etapa que ocorre transformações mais elaboradas e definitivas. 

Com isso, o primeiro passo desse desafio foi realizar a união dos dados gerados na sprint anterior. Para isso, foi processado um Job no AWS Glue. Foram definidos três caminhos:

- `TRUSTED_PATH_API`: caminho de origem dos dados processados da API contidos na camada Trusted.
- `TRUSTED_PATH_CSV`: caminho de origem dos dados processados do CSV contidos na camada Trusted.
- `STAGING_PATH`: caminho de destino do resultado do processamento do job atual. 

Na imagem abaixo podemos ver parte do código: 

![imagem_job_staging_01](../evidencias/08_job_camada_staging.png)

- Nas linhas 30 e 36 foi realizada a seleção das colunas necessárias para o processamento dos dados de acordo com o tipo da linha da análise escolhida, tanto da API quanto do CSV. E é exatamente por isso que mais colunas da DataFrame da API foram selecionadas.
- Na linha 40 foi realizado a filtragem de valores nulos da coluna "budget", pois é com base nesses dados que minha análise será fundamentada. 
- Nas linhas 41 e 47 foi a criação de uma coluna `idFilmes` em ambos DataFrames, pois eles possuiam uma mesma coluna de ids com nome diferente, dessa forma foi possível fazer a união desses dados. Com isso, foi realizado a remoção do prefixo "tt" dos dados dessas colunas com `regexp_replace`, além da remoção das colunas originais. 
- Uma observação para o nome do job. Ele não foi escolhido da melhor forma pois nas tentativas anteriores eu acreditava ser possível fazer todo o desafio em apenas um job, ou seja, todo o processamento de uma vez só. Encontrei alguns problemas no caminho e após achar a solução, mantive esse job com o código corrigido e não me atentei ao nome. 


![imagem_job_staging_02](../evidencias/09_job_camada_staging_2.png)

- Na linha 52 foi realizada a união dos DataFrames. Com `allowMissingColumns=True` foi possível permitir que caso alguma coluna estivesse faltando em um dos DataFrames, ela seria automaticamente preenchida com valores nulos.
- Na linha 53 foi removido as duplicatas com base na coluna `idFilmes`, pois a análise final tem como objetivo prioritário trabalhar os dados dos filmes referentes a voto, popularidade e orçamento. 
- Na linha 54 foi gerado o particionamento da gravação desses dados. Diferentemente dos códigos anteriores, optei por utilizar o módulo `datetime` contido no python. Nos jobs anteriores eu estava enfrentando muitos problemas de particionamento com data, principalmente na questão da nomeação dos diretórios e subdiretórios, dessa forma optei por utilizar algo que eu já tinha mais familiaridade e que deixasse o código mais simples. 

### **3.1. Resultado do processamento**

Após o processamento do job, a camada Staging ficou da seguinte forma no datalake:

![imagem_bucket_camada_staging](../evidencias/02_camada_staging.png)

Dessa forma, foi desenvolvido um crawler para a criação da tabela unificada. 

## **4. Camada Refined**

A camada Refined é uma área em que os dados passam por transformações, estão organizados, estruturados e limpos, pronta para a análise. 

O segundo passo desse desafio foi a criação da camada Refined e, assim, a estruturação dos dados em uma modelagem dimensional. Para isso, foi elaborado previamente um diagrama contendo o Modelo de Dados, como podemos visualizar a seguir:

![imagem_dimensionamento](../evidencias/00_modelo_dimensional.png)

Este modelo foi estruturado de acordo com o padrão _star schema_. Contém uma tabela fato em que os dados quantitativos estão armazenados, ou seja, os ids. Por conta da análise focar em métricas quantitativas, como orçamento, notas de avaliação, retorno financeiro e popularidade, foram definidas 4 tabelas dimensão: Tempo, Localização, Filme e Popularidade. 

### **4.1. Código desenvolvido**

Agora com o modelo dimensional definido, iniciou-se o desenvolvimento do segundo job. Na imagem abaixo podemos ver a primeira parte do código:

![imagem_job_refined_01](../evidencias/10_job_camada_refined.png)

- A primeira observação vai para os imports: muito desses imports não foram utilizados no código por descuido com as mudanças durante o desenvolvimento. 
-
-
-
-


### **5. Crawlers**

Os crawlers são ferramentas automatizadas com o objetivo de explorar os dados armazenados. No nosso caso, esses dados estão no S3. Ele é capaz de realizar automaticamente a estrutura (esquema) desses dados e criar tabelas no Glue Data Catalog.

Neste desafio, optei pela criação de dois crawlers, um para os dados extraídos do CSV e outro para os dados extraídos dos arquivos JSON.

![imagem_crawler](../evidencias/13_crawlers.png)

A criação desses crawlers são bem simples, basicamente bastou informar corretamente o caminho do S3 e executar. Podemos ver o resultado no Athena:

![imagem_athena](../evidencias/14_consulta_athena.png)

Na query acima, foi realizado uma consulta com join entre as tabelas para verificar se estava tudo correto. E essa foi a última estapa deste desafio.
