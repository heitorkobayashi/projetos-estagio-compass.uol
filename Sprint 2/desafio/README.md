# **Sprint 2: Desafio**

## **1. Objetivos**

Este desafio teve como objetivo normalizar uma base de dados aplicando as regras das formas normais e, a partir dessa base normalizada no Modelo Relacional, montar o Modelo Dimensional.

Dessa forma, o desafio se dividiu em 2 etapas:

1. Normalizar Base de Dados: **[Clique aqui](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/desafio/scripts/script_modelo_relacional.sql)** para acessar o código fonte do Modelo Relacional.

2. Modelo Dimensional baseado no Modelo Relacional: **[Clique aqui](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/desafio/scripts/script_modelo_dimensional.sql)** para acessar o código fonte do Modelo Relacional.

## **2. Preparação**

Antes de iniciar o desafio, foi realizada a preparação. Desta vez era simples, apenas o download do arquivo `concessionaria.zip`, download de um cliente SQL, no caso a escolha foi o `DBeaver`, e a conexão ao banco de dados.

## **3. Normalização**

Os dados contidos no arquivo `.zip` não estavam tão organizados. Para isso, o primeiro passo a ser feito foi a normalização, que nada mais é a organização dos dados, diminuindo redundância, anomalias, erros e garantindo a integridade dos dados. 

O primeiro passo é entender a estrutura da tabela. Isso ajuda a identificar o que precisa de fato ser normalizado.

A primeira forma normal 1FN já estava realizada, então bastou atentar-se para as formas seguintes, 2FN e 3FN. Dessa forma, separei as tabelas e colunas da seguinte forma:

- tb_locacao: `idLocacao`, `idCliente`, `idVendedor`, `idCarro`, `idCombustivel`, `horaLocacao`, `qtdDiaria`, `vlrDiaria`, `horaEntrega`, `dataLocacao`, `dataEntrega`
- tb_cliente: `idCarro`, `nomeCliente`, `cidadeCliente`, `estadoCliente`, `paisCliente`
- tb_vendedor: `idVendedor`, `nomeVendedor`, `sexoVendedor`, `estadoVendedor`
- tb_carro: `idCarro`, `marcaCarro`, `modeloCarro`, `kmCarro`, `anoCarro`, `classiCarro`, `idCombustivel`
- tb_combustível: `idCombustivel`, `tipoCombustivel`

A 3FN não foi necessário ser executada. Na próxima imagem podemos ver a 2FN em ação:

![imagem_normalizacao](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/desafio/analise_e_normalizacao.png)

Para facilitar a visualização desses dados, nesse primeiro momento, optei pela utilização do [`dbdiagram.io`](https://dbdiagram.io/):

![imagem01](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/evidencias/01_diagramacao_modelo_relacional.png)

Com isso, foi definido as chaves primárias e chaves estrangeiras, sendo elas:

| Tabela             | Coluna                                                | Tipo de chave      |
| :------------------| :-----------------------------------------------------| :------------------|
|  tb_locacao      | `idLocacao`                                             | chave primária     |
|  tb_locacao      | `idCliente`, `idVendedor`, `idCarro`, `idCombustivel`   | chave estrangeira  |
|  tb_cliente      | `idCliente`                                             | chave primária     |
|  tb_vendedor     | `idVendedor`                                            | chave primária     |
|  tb_carro        | `idCarro`                                               | chave primária     |
|  tb_carro        | `idCombustivel`                                         | chave estrangeira  |
|  tb_combustivel  | `idCombustivel`                                         | chave primária     |

Realizada a normalização, podemos seguir com a criação das tabelas.

## **4. Etapa 1: Modelo Relacional - Criação de Novas Tabelas**

Nesta etapa, foi realizado os comandos para a criação das novas tabelas. Na imagem abaixo podemos ver com mais detalhes:

![imagem_02](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/evidencias/02_criacao_tabelas.png)

Na sequência, a criação da tabela `tb_locacao`

![imagem_03](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/evidencias/03_criacao_tb_locacao.png)
- Aqui podemos observar a realização de um "backup" da tabela original, para segurança dos dados. 
- A adição das colunas `dataLocacao` e `dataEntrega` após a criação da tabela foi uma escolha baseada no tipo de dado origina, o qual continha vírgulas e não se encontrava no formato YYYY-MM-DD. Dessa forma, essa decisão facilitou o tratamento desses dados posteriormente.

### **4.1. Transferência dos Dados**

Agora, foi necessário transferir os dados da tabela `tb_locacao_temp` para as novas tabelas, como podemos ver a seguir:

![imagem_04](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/evidencias/04_transferencia_dados.png)

![imagem_05](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/evidencias/05_transferencia_dados_locacao.png)

### **4.2. Tratamento dos Dados**

Algumas colunas continham dados com valores anômalos. Para resolver este problema, pelo banco não conter muitos dados, optei por fazer uma atualização dos valores das colunas, corrigindo os dados manualmente. 

![imagem_06](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/evidencias/06_adicao_datas.png)
- As datas na tabela original estavam no formato "20,150,110".
- A subquery `numbered` cria uma tabela temporária que realiza uma consulta que escolhe a cada linha (_rowid_) e o valor da coluna `dataLocacao` de cada registro da tabela `tb_locacao`, sendo associado com o _id_ de cada linha. 
- O comando `case` é utilizado para verificar os valores da coluna `idLocacao`.
- Além da coluna `dataLocacao`, essa lógica foi utilizada para as colunas `dataEntrega` e `kmCarro`.


### **4.3. Criação dos Índices**

Os índices são fundamentais para melhorar a performance das consultas. Dessa forma, foram criados os seguintes índices:

![imagem_07](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/evidencias/07_exclusao_e_index.png)

### **4.4. Diagrama do Modelo Relacional**

Após todas essas etapas, o resultado obtido foi este:

![imagem_08](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/evidencias/08_modelo_relacional.png)

## **5. Etapa 2: Modelo Dimensional**

Para montar uma tabela no modelo dimensional a partir de um banco relacional, é muito importante entender o que são as tabelas fatos e as tabelas dimensões.

A **tabela fato**, como o próprio nome diz, contém tudo aquilo que é referente a situações que acontecem, como métricas e eventos, como número de vendas, valores, quantidades, entre outros.

A **tabela dimensão** possui também um nome sugestivo, ela fornece todo o contexto para a tabela fato, como datas, clientes, vendedores, produtos etc.

Existem alguns esquemas para o Modelo Dimensional. Os mais utilizados são o _Star Schema_ e o _Snowflake Schema_. Para este desafio, foi utilizado o Star Schema, devido a facilidade.

### **5.1. Criação das Tabelas de Dimensões**

As tabelas de dimensões foram organizadas da seguinte forma:

- dim_tempo: `idTempo`, `data`, `ano`, `mes`, `semana`, `dia`, `qtdDiaria`, `horario`
- dim_localizacao: `idLocalizacao`, `pais`, `estado`, `cidade`
- dim_cliente: `idCliente`, `Cliente`
- dim_vendedor: `idVendedor`, `vendedor`, `genero`, `estado`
- dim_carro: `idCarro`, `marca`, `modelo`, `quilometros`, `ano`, `classificacao`, `combustivel`

Na imagem abaixo, podemos ver a criação das tabelas:

![imagem_09](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/evidencias/09_criacao_tabelas_dim.png)

### **5.2. Criação da Tabela Fato**

A tabela fato foi organizada da seguinte forma:

- fato_locacao: `idLocacao`, `idCliente`, `idVendedor`, `idCarro`, `idTempo`, `idLocalizacao`, `quantidade`, `valor`

Na imagem abaixo, podemos ver a criação da tabela:

![imagem_10](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/evidencias/10_criacao_tabela_fato.png)

### **5.3. Diagrama do Modelo Dimensional**

Após todas essas etapas, o resultado obtido foi este:

![imagem_11](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/evidencias/11_modelo_dimensional.png)

### **5.4. Criação dos Views**

As views são consultas que podem ser tratadas como tabelas virtuais, permitindo o acesso simplificado a dados complexos. 

Dessa forma, para facilitação dos dados na tabelas do modelo dimensional, foram criadas views de cada tabela. Você pode conferí-las **[neste link](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/desafio/scripts/script_views_modelo_dimensional.sql)**

Na imagem abaixo, podemos ver o código para criação dessas views. A última imagem é o resultado de uma delas.

![imagem_12](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/evidencias/12_criacao_views.png)

![imagem_13](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/evidencias/13_criacao_views_2.png)

![imagem_14](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/evidencias/14_resultado_view_tempo.png)

### **6. Dificuldades e Considerações Finais**

Durante o desenvolvimento do desafio, em alguns momentos, enfrentei algumas dificuldades que impactaram o progresso.

Uma das primeiras adversidades foi a inserção dos dados nas tabelas. Embora eu tivesse planejado automatizar boa parte do processo, nem tudo saiu conforme o esperado. Algumas rotinas de automação não funcionaram. Isso me obrigou a encontrar uma maneira manual de lidar com a inserção, o que, além de aumentar o tempo necessário, exigiu um cuidado maior para garantir a consistência e integridade das informações. Essa solução alternativa trouxe desafios adicionais, mas foi essencial para manter o fluxo de trabalho.

Outro ponto de dificuldade foi a compreensão do modelo dimensional. Vindo de um contexto mais familiar com o modelo relacional, o modelo dimensional me pareceu bastante abstrato no início, o que demandou tempo de estudo e aprofundamento. A transição entre os dois modelos não foi simples, exigindo que eu reconsiderasse algumas abordagens, principalmente no que diz respeito ao relacionamento entre as tabelas e à forma de organizar as informações para análise posterior. O processo de assimilação desse novo conceito foi mais demorado do que eu previa.

O uso do DBeaver trouxe vários desafios. Mesmo sendo uma boa ferramenta, a manipulação de dados nem sempre foi tão intuitiva. Em vários momentos enfrentei dificuldades para realizar operações que, em outras ferramentas, seriam mais simples. Isso aumentou a curva de aprendizado e exigiu mais tempo para ajustes e correções de pequenos erros. Apesar desses entraves, consegui realizar as tarefas necessárias, mesmo não estando totalmente satisfeito com elas, principalmente sobre a elaboração desse readme.

Apesar dos desafios enfrentados ao longo do desafio, considero que ele foi uma oportunidade rica de aprendizado. A inserção manual de dados, o estudo do modelo dimensional e o uso de ferramentas como o DBeaver me ajudaram a desenvolver uma visão mais técnica e prática sobre modelagem de dados. Embora o tempo tenha sido apertado, considero que o processo me trouxe habilidades valiosas que transpassam as habilidades técnicas. Mais uma vez a comunicação com as Squads e as monitorias foram de muito valor.

## **8. Referências**

Além do próprio conteúdo contido na Udemy, tanto do curso de SQL quanto das apresentações contidas nos slides, utilizei das seguintes referências:

- BÓSON TREINAMENTOS. **Modelagem de Dados - O Modelo Relacional - Introdução.** YouTube, 23 fev. 2021. Disponível em: https://www.youtube.com/watch?v=hGstS10kCPM. Acesso em: 4 set. 2024.

- Decomplexify. **Learn Database Normalization.** YouTube, 16 jul. 2020. Disponível em: https://www.youtube.com/watch?v=GFQaEYEc8_8. Acesso em: 13 de set. 2024.

- EBAC. **Normalização de bases de dados.** Disponível em: https://ebaconline.com.br/blog/normalizacao-de-bases-de-dados. Acesso em: 12 de set. 2024.


