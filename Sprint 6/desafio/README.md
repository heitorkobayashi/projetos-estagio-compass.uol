# **Sprint 6: Desafio**

## **1. Objetivos**

Este desafio teve como objetivo a ingestão de arquivos CSV em um Bucket no `S3`. Essa é a primeira etapa do Desafio Final.

Para isso, foi necessário construir um código Python que foi executado dentro de um conteiner Docker para carregar os dados locais dos arquivos `series.csv` e `movies.csv` para o bucket.

Clique nos seguintes links para acessar os respectivos códigos e arquivos:

- [Script Python](/Sprint%206/desafio/entrega_1/desafio_sprint06_script.py)
- [Dockerfile](/Sprint%206/desafio/entrega_1/Dockerfile)

Obs.: Os arquivos `series.csv` e `movies.csv` não se encontram no repositório pois eles são muito pesados e estava dando erro ao commitá-los.


## **2. Definição de Tema**

Antes de iniciar o desenvolvimento do desafio, foi solicitado a realização de uma questão que é a elaboração do tema da análise do desafio final. 

O meu desafio abordará a **análise da relação entre orçamento e qualidade em filmes de ação**.

Esta análise pretende explorar em como o orçamento impacta a qualidade percebida dos filmes de ação, comparando produções de alto e baixo orçamento.

Com base em uma experiência prévia no audiovisual e no cinema brasileiro, tive a oportunidade de participar de diversos projetos de baixo a médio orçamento obtendo resultados positivos por parte da crítica. Muitas vezes, diversos filmes fora do eixo hollywoodiano lidam com restrições financeiras e dificuldades de produção, dessa forma, pretendo observar e responder perguntas como:

- Filmes de alto orçamento são realmente melhores avaliados?
- Como filmes com orçamento reduzido, mas bem avaliados, conseguem obter boas avaliações com recursos escassos?
- O que as produções de baixo orçamento podem conquistar em comparação com produções de grande orçamento?

A maior motivação é entender como filmes de ação de menor orçamento podem competir com grandes produções, que muitas vezes possuem recursos em alta quantidade e obtem resultados negativos. 

## **3. Desenvolvimento**

### **3.1. Criação do bucket**

Para começar o desafio, o primeiro passo foi a criação do bucket, como podemos ver nas imagens a seguir:

![imagem_criacaobucket](/Sprint%206/evidencias/01_desafio_criacao_bucket.png)

### **3.2. Criação do script Python**

Agora com o bucket criado, podemos passar para o próximo passo, a criação do Script. 

Na imagem abaixo podemos ver:

![imagem_script1](/Sprint%206/evidencias/05_desafio_script_01.png)

- Importação da biblioteca `boto3` e `datetime`
- Configuração do Bucket no S3 que tem a função de estruturar os caminhos dos arquivos.
- Definição do caminho local dos arquivos CSV.
- Criação de um dicionário `categoria_paths` para definir os subdiretórios no bucket e organizar os arquivos de acordo com a categoria.

Em seguida, temos: 

![imagem_script2](/Sprint%206/evidencias/06_desafio_script_02.png)

- A variável `hoje` utiliza a data atual para criar a estrutura de caminho solicitada no desafio, com o ano, mês e dia em que é realizado o upload. 
- As credenciais da AWS foram armazenadas em variáveis. Infelizmente obtive problemas de credencial na etapa do Docker, então optei pela utilização das credenciais no próprio código. 

Por fim:

![imagem_script3](/Sprint%206/evidencias/07_desafio_script_03.png)

- Definição de duas funções:

    - A função `upload_arquivos` recebe o caminho de arquivo local e o caminho de destino no S3, e então realiza o upload dos arquivos no bucket. Ela contém também uma mensagem de sucesso e de erro caso o upload falhe. 
    - A segunda função `main` ela cria o cliente S3 e constrói o caminho de destino com a estrutura solicitada, utilizando as variáveis definidas anteriormente. Por fim, chama a função anterior para fazer o upload de cada arquivo no caminho correto.
- Execução do script chamando a função `main` diretamente.

### **3.3. Criação do Dockerfile e execução do script**

Tendo o script finalizado, bastava a criação do Dockerfile e fazer a execução do container, como podemos ver na imagem abaixo. Você pode conferir o Dockerfile no link descrito na primeira seção deste readme.

![imagem_docker](/Sprint%206/evidencias/04_desafio_terminal_docker.png)

- Além da utilização das credenciais, foi utilizado a flag -v para fazer o mapeamento dos arquivos localmente e indicar o local em que o conteiner irá acessar os arquivos e onde montará esses arquivos.

### **3.4. Upload no bucket**

Com o upload tendo sucesso, podemos visualizar os arquivos nos caminhos definidos lá no bucket do S3, finalizando a primeira etada do desafio final:

![imagem_bucket_movies](/Sprint%206/evidencias/02_desafio_upload_movies.png)
![imagem_bucket_series](/Sprint%206/evidencias/03_desafio_upload_series.png)