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

Para facilitar a visualização desses dados, nesse primeiro momento, optei pela utilização do [`dbdiagram.io`](https://dbdiagram.io/), como mostra a imagem a seguir:

![imagem01](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/desafio/evidencias/01_diagramacao_modelo_relacional.png)

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

## **4. Etapa 1: Modelo Relacional - Criação de novas tabelas**

Nesta etapa, foi realizado os comandos para a criação das novas tabelas. Na imagem abaixo podemos ver com mais detalhes:

![imagem_02](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/desafio/evidencias/02_criacao_tabelas.png)

Na sequência, a criação da tabela `tb_locacao`

![imagem_03](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/desafio/evidencias/03_criacao_tb_locacao.png)
- Aqui podemos observar a realização de um "backup" da tabela original, para segurança dos dados. 
- A adição das colunas `dataLocacao` e `dataEntrega` após a criação da tabela foi uma escolha baseada no tipo de dado origina, o qual continha vírgulas e não se encontrava no formato YYYY-MM-DD. Dessa forma, essa decisão facilitou o tratamento desses dados posteriormente.

### **4.1. Transferência dos dados**

Agora, foi necessário transferir os dados da tabela `tb_locacao_temp` para as novas tabelas, como podemos ver a seguir:

![imagem_04](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/desafio/evidencias/04_transferencia_dados.png)

![imagem_05](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/desafio/evidencias/05_transferencia_dados_locacao.png)

### **4.2. Tratamento dos dados**

Algumas colunas continham dados com valores anômalos. Para resolver este problema, pelo banco não conter muitos dados, optei por fazer uma atualização dos valores das colunas, corrigindo os dados manualmente. 

![imagem_06](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%202/desafio/evidencias/06_adicao_datas.png)
- As datas na tabela original estavam no formato "20,150,110".
- A subquery `numbered` cria uma tabela temporária que realiza uma consulta que escolhe a cada linha (_rowid_) e o valor da coluna `dataLocacao` de cada registro da tabela `tb_locacao`, sendo associado com o _id_ de cada linha. 
- O comando `case` é utilizado para verificar os valores da coluna `idLocacao`.
- Além da coluna `dataLocacao`, essa lógica foi utilizada para as colunas `dataEntrega` e `kmCarro`.


### **4.3. Criação dos índices**

![imagem_07]()


### **4.4. Diagrama do Modelo Relacional**

![imagem_08]()

## **5. Etapa 2: Modelo Dimensional**

### **5.1. Criação das tabelas dimensão**

### **5.1. Criação das tabelas dimensão**

### **5.2. Criação da tabela fato**

### **5.3. Diagrama do Modelo Dimensional**

### **5.4. Criação dos views**

### **6. Dificuldades e Considerações finais**

## **8. Referências**

- 