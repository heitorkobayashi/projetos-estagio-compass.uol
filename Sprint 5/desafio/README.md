# **Sprint 5: Desafio**

## **1. Objetivos**

Este desafio teve como objetivo a prática e manipulação de arquivos diretamente no `S3`. 

Para isso, foi proposta a procura de um arquivo CSV ou JSON no portal de dados do Governo Brasileiro. Com um script de Python, foi solicitado o carregamento do arquivo para um bucket novo, utilizando a biblioteca `boto3`. Com um outro script Python e a partir do arquivo que está dentro do S3, foi pedido a criação de um dataframe com _pandas_ ou _polars_ e a execução de algumas manipulações, como funções de agregação, funções condicionais etc. 

Após a conclusão dessas etapas, foi solicitado que o arquivo resultante das manipulações fosse salvo no formato .csv e enviado para o mesmo bucket criado nesse desafio, utilizando `boto3`.

Clique nos seguintes links para acessar os respectivos códigos e arquivos:

- [Script 1](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%205/desafio/script_1.py)
- [Script 2](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%205/desafio/script_2.py)
- [Arquivo CSV](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%205/desafio/lancamentos_comerciais_por_distribuidoras.csv)
- [Arquivo CSV manipulado](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%205/desafio/resultado_manipulacoes.csv)


## **2. Preparação**

Para a resolução do desafio, foi necessário a preparação do ambiente, ou seja, a instalação do _boto3_ e configuração das credenciais da AWS. 

O conjunto de dados escolhido foi o `lancamentos_comerciais_por_distribuidoras.csv`, disponibilizado pela Ancine (Agência Nacional do Cinema)

## **3. Desenvolvimento**

Para começar o desafio, o primeiro passo foi a criação do bucket, como podemos ver nas imagens a seguir:

![imagem_01](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%205/evidencias/desafio_01.png)

![imagem_02](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%205/evidencias/desafio_02.png)

Agora com o bucket criado, podemos passar para o próximo passo, a criação do Script 1 para carregamento do arquivo dentro do novo bucket utilizando Boto3:

![imagem_03](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%205/evidencias/desafio_03.png)

Para este primeiro script, foi utilizando a importação da biblioteca Boto3, permitindo a interação com os serviços da AWS, no caso, o S3. Para isso, foi necessário criar uma instância de sessão baseada no perfil configurado `heitorkobayashi`.

Com as variáveis definidas, foi possível definir o nome do bucket onde o arquivo seria enviado, assim como o caminho absoluto do arquivo no meu sistema local. 

- o prefixo `r` foi utilizado antes da string para manter o caminho como está, com as barras invertidas.
- Foram utilizados tratamento de execções para lidar com possíveis erros e falhas na conexão, pois infelizmente eu estava enfrentando muitos problemas com o acesso à AWS, o que tomou muito do meu tempo.

Na imagem a seguir, podemos ver o carregamento realizado com sucesso: 

![imagem_04](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%205/evidencias/desafio_04.png)

Dessa forma, agora bastava a criação do Script 2 e a realização das queries solicitadas:

![imagem_05](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%205/evidencias/desafio_05.png)

Para este segundo Script, foram importadas as bibliotecas pandas e boto3, assim como a linha:

```
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
```

- esse código foi utilizado para lidar com os erros de autenticação que eu estava tendo, facilitando encontrar os problemas e encontrar de maneira mais rápida a solução

Para as funções solicitadas, eu optei por utilizar funções simples, como a manipulação de datas, conversão de strings e de agregação. O maior trabalho foi a conversão e limpeza de dados, que demandou mais tempo de análise.

- O resultado dessas queries foram concatenados em um unico arquivo CSV.

No último trecho do código temos várias exceções para lidar com os erros que eu estava tendo de credenciais da AWS. Dessa forma ficou mais fácil de localizar os erros e entender o que precisava ser feito para corrígilos, como a instalação da AWS CLI e bibliotecas como _fsspec_ e _s3fs_ para que fosse possível o Pandas acessar o Amazon S3 como um sistema de arquivos.

Na imagem a seguir, podemos ver o carregamento do arquivo .csv manipulado com sucesso:

![imagem_06](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%205/evidencias/desafio_06.png)

Para finalizar, todos os arquivos e o bucket foram deletados:

![imagem_07](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%205/evidencias/desafio_07.png)

![imagem_09](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%205/evidencias/desafio_09.png)

