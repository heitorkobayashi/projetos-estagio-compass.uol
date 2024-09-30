# **Sprint 3: Desafio**

## **1. Objetivos**

Este desafio teve como objetivo ler o arquivo de estatísticas da _Play Store_, o `googleplaystore.csv`, processar e gerar os gráficos de análise solicitados através do Jupyter.  

## **2. Preparação**

Para a resolução do desafio, foi necessário a preparação do ambiente. Optei por utilizar o Jupyter dentro do VS Code por estar familiarizado com o editor. Acesse o código [clicando aqui](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/desafio/entregaveis/desafio.ipynb) 

## **3. Desenvolvimento**

### **3.1. Importação das bibliotecas**

Antes de realizar o tratamento e a análise dos dados, é necessário fazer a importação das bibliotecas que serão utilizadas. Essas bibliotecas já estavam instaladas previamente no sistema.

![img_01](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/01_importando_bibliotecas.png)

A utilização do `mticker` se deu para formatar e personalizar os rótulos dos eixos dos gráficos, os deixando mais apresentáveis.

### **3.2. Leitura do arquivo .csv**

Para realizar as análises, foi iniciado o carregamento do dataset em um DataFrame, como pode ser visto na imagem abaixo:

![img_02](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/02_leitura_arquivo_csv.png)

- A utilização do `display`, `head` e `info` se deu para faciltiar a visualização de como os dados estavam sem tratamento prévio, e assim, poder entender quais informações estavam contidas no arquivo.

### **3.3. Tratamento dos dados**

Com o objetivo de facilitar a análise e trazer uma melhor qualidade nos dados, foi realizada a etapa de tratamento de dados, que envolveu a exclusão dos nulos, conversão dos tipos e exclusão dos dados duplicados.

### **3.3.1. Exclusão e preenchimento dos nulos**

A função `dropna(subset=)` remove todas as linhas onde existem valores nulos. Nesse caso, basta especificar as colunas desejadas. Para a coluna Rating, houve o preenchimento dos dados com a média de todos os demais valores, para isso a função `fillna()` + `.mean` foi utilizada. 

![img_03](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/03_exclusao_dos_nulos.png)

### **3.3.2. Correção dos tipos de dados das colunas**

Além de verificar e corrigir os tipos de dados das colunas, foi realizada a limpeza dos dados, removendo vírgulas e demais espaços que poderiam ser prejudiciais.

![img_04](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/04_conversao_dos_tipos.png)

- Para a coluna Size, foi utilizado uma lógica em que além de remover letras contidas nos dados, fazia a conversão para o tamanho original do dado em Megabytes. 

### **3.3.3. Exclusão dos dados duplicados**

Tendo o objetivo de ter mais precisão nas análises, eliminando as redundâncias e facilitando a visualização, foi realizada a exclusão dos dados duplicados com a função `drop_duplicates()`. 

![img_05](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/05_exclusao_duplicados.png)

- Para a coluna App houve a intenção de reafirmar o `keep='first`, para realmente manter apenas a primeira ocorrência de cada duplicata.
- Para facilitar a visualização, os dados foram formatados para serem visualizados com duas casas decimais.

## **4. Análise dos dados**

### **4.1. Top 5 aplicativos mais instalados**

Para criar o gráfico de barras em que seleciona os top 5 aplicativos com maior número de instalações, foi utilizado o código a seguir:

![img_06](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/06_top_5_apps_mais_instalados.png)

- Para a melhor visualização dos dados, foi escolhido a geração de um gráfico de barras horizontal com `plt.barh`. 
- O loop `for` foi utilizado para adicionar o número de instalações ao lado de cada barra com a visualização em bilhões.
- O gráfico foi personalizado para garantir uma boa visualização.

![gráfico_1](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/desafio_top_5_aplicativos.png)

### **4.2. Frequência de categorias de aplicativos**

Para gerar o gráfico de pizza que mostra a frequencia das categorias dos aplicativos da Play Store, foi utilizado o código a seguir:

![img_07](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/07_frequencia_categorias_apps.png)

- A função `value_counts()` conta quantas vezes cada categoria aparece.
- A variável `limite_outros` foi criada para definir um limite e agrupar as categorias com menos de 200 ocorrências, criando uma única categoria chamada Outros.
- Para criar um gráfico de pizza, utilizou-se o `plt.pie`. Cada fatia representa uma categoria de aplicativo.
- Pensando numa melhor visualização, foram utilizados alguns comandos como:
    - `autopct=%0.1f%%` que exibe a porcentagem com apenas uma casa decimal;
    - `wedgeprops={'edgecolor': 'black'}` que adiciona bordas em cada fatia;
    - `pctdistance=0.75` que coloca o texto da porcentagem mais aos cantos do gráfico.

![gráfico_2](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/desafio_frequencia_categoria_aplicativos.png)

### **4.3. Aplicativo mais caro da plataforma**

Para exibir o aplicativo mais caro da plataforma, foi utilizado o código a seguir:

![img_08](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/08_app_mais_caro.png)

- A função `nlargest()` seleciona o dado com o maior valor da coluna.
- O `1` delimita que será selecionada apenas uma linha.

### **4.4. Aplicativos classificados como 'Mature 17+'**

Para exibir os aplicativos classificados como 'Mature 17+', foi utilizado o código a seguir:

![img_09](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/09_apps_mature_17.png)

- Para filtrar os aplicativos, foi utilizado a variável `apps_mature_17`.
- O `shape[0]` faz a "contagem" do número de linhas que representa o total de aplicativos filtrados.

### **4.5. Os 10 aplicativos com maior número de reviews**

Para exibir os 10 aplicativos com maior número de reviews, foi utilizado o código a seguir:

![img_10](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/10_top_apps_numeros_reviews.png)

- A função `nlargest()` seleciona o dado com o maior valor da coluna.
- O `10` delimita que será selecionada apenas as 10 primeiras linhas.

### **4.6. Os 10 aplicativos piores avaliados**

Para exibir os 10 aplicativos piores avaliados, foi utilizado o código a seguir:

![img_11](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/11_top_piores_apps.png)

- A função `nsmallest()` tem a função similar da função anterior, mas nesse caso, ela seleciona os dados com os menores valores da coluna.
- O `10` delimita que será selecionada apenas as 10 primeiras linhas.

### **4.7. Aplicativo com a atualização mais antiga**

Para exibir o aplicativos com a atualização mais antiga da plataforma, foi utilizado o código a seguir:

![img_12](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/12_apps_com_atualizacao_mais_antiga.png)

- Com a variável `app_nome` e com o `.values` é possível extrair o nome do aplicativo do DataFrame.
- O valor da coluna Last Update foi convertido para uma string, sendo assim possível exibir o resultado.

### **4.8. Mapa de calor do número de aplicativos instalados por categoria**

Para criar um mapa de calor exibindo o número de aplicativos instalados pela categoria, foi utilizado o código a seguir:

![img_13](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/13_numero_de_instalacoes_por_categoria.png)

- A variável `instalacao_categoria` foi necessária para agrupar os dados pela coluna Category e, para cada categoria, calcular a soma total de instalações. Além disso, foi preciso ordenar o em ordem descrescente, baseando-se no número de instalações realizadas, assim as categorias com mais intalações aparecerão em primeiro lugar.
- O `plt.imshow` cria uma imagem a partir da lista de instalações, com isso é possível a visualização do mapa de calor.
- Novamente o `mticker` foi necessário para formatar os números como bilhões.

A escolha de um gráfico em Mapa de calor foi escolhida pela eficácia em sua visualização, sem contar por ser um tipo de gráfico diferente dos outros, chamando bastante a atenção. 

![gráfico_3](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/desafio_numero_de_instalacoes_por_categoria.png)

### **4.9. Gráfico de número de instalações ao longo do tempo**

Para criar um gráfico mostrando o número total de instalações ao longo do tempo, foi utilizado o código a seguir:

![img_14](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/14_instalacoes_ao_longo_do_tempo.png)

- A variável `instalacoes_por_data` tem função parecida com a variável do gráfico anterior, com a diferença de agrupamento pelo ano extraido da coluna Last Update.
- O `plt.fill_betwenn` cria uma area preenchida sob a linha do gráfico, deixando-o mais visual.
- Novamente o `mticker` foi necessário para formatar os números como bilhões.

![gráfico_4](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%203/evidencias/desafio_instalacoes_por_tempo.png)

## **5. Considerações finais**

Durante o desenvolvimento deste desafio, enfrentei algumas dificuldades que impactaram no meu progresso e aprendizado. Uma das primeiras adversidades foi a manipulação dos dados na biblioteca Pandas. Embora eu tivesse uma compreensão básica de como realizar operações como agrupamento e filtragem, algumas operações não saíram conforme o esperado. Isso me forçou a investigar mais a fundo as funcionalidades do Pandas e a adotar abordagens diferentes.

Outro ponto desafiador foi a criação de visualizações eficazes. A utilização dos gráficos com o Matplotlib foi fundamental, mas bem dificultosa em relação à formatação de eixos. Entretanto, percebo que aprendi a importância de escolher cores e formatos que facilitassem a interpretação dos dados, um aspecto que inicialmente subestimei.

A compreensão da notação correta e das unidades de medida, como bilhões e milhões foi bem desafiador. Entendo que não era algo crucial, mas me dediquei para conseguir entregar esses eixos corretamente formatados.

## **6. Referências**

- CS DOJO. **Intro to Data Analysis / Visualization with Python, Matplotlib and Pandas | Matplotlib Tutorial.** YouTube, 11 jun. 2018. Disponível em: https://www.youtube.com/watch?v=a9UrKTVEeZA. Acesso em: 25 set. 2024.

- DESIGN4U. **Colors.** Disponível em: https://colors.design4u.jp. Acesso em: 26 set. 2024.

- HASHTAG TREINAMENTOS. **Minicurso Python para Automação.** Disponível em: https://pages.hashtagtreinamentos.com/minicurso-python-automacao-obrigado?blog=1n4033rer&video=3dep762tr. Acesso em: 23 set. 2024.

- MATPLOTLIB. **Colormaps in Matplotlib.** Disponível em: https://matplotlib.org/stable/users/explain/colors/colormaps.html. Acesso em: 25 set. 2024.








