# **Sprint 1: Desafio**

## 1. Objetivos

Este desafio teve como objetivo a criação de dois scripts que automatizassem a geração de relatórios de vendas a partir de um arquivo `.cvs`, com execução durante 4 dias seguidos.

O primeiro script, o qual chamaremos de [Script 1](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/desafio/entregaveis/ecommerce/processamento_de_vendas.sh), realiza a criação de diretórios e subdiretórios, a cópia do arquivo `.csv` para arquivos de backup junto com a moção desses arquivos para determinados diretórios, além da extração de dados deste arquivo e a criação de um `relatorio.txt` contendo todas essas informações. Já o segundo script, [Script 2](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/desafio/entregaveis/ecommerce/consolidador_de_processamento_de_vendas.sh), teve como função a junção de todos os relatórios gerados a partir do script anterior e, assim, criar um arquivo chamado `relatorio_final.txt`
## 2. Preparação

Antes de iniciar o script em si, foi realizada a preparação da área de trabalho, ou seja, a criação dos diretórios necessários para a execução deste desafio.

### 2.1. Criação do diretório ecommerce

Para criar o diretório `ecommerce` foi utilizado o comando `mkdir ecommerce`. O arquivo `dados_de_vendas.csv` foi inserido manualmente no linux. Com o comando `ls` pode-se listar os diretórios e arquivos existentes, como mostra a imagem abaixo:

![imagem_01](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/evidencias/01_criacao_pasta_ecommerce.png) 


## 3. Criação do Script 1

Nesta etapa, no processo de criação do script, foi dada a preferência por desenvolvê-lo em etapas para garantir que o caminho estava correto e evitar surpresas ao final do código.

### 3.1 Criação dos subdiretórios

O primeiro passo deste script foi a criação dos subdiretórios `vendas` e `backup`, além da realização de uma cópia do arquivo `dados_de_vendas.csv` para a pasta `vendas`.

- Com o comando `cd` é definido onde o script será executado.
- Sabendo que o script será realizado mais que uma vez, com o `mkdir -p` é possível realizar a criação da pasta vendas e prevenir erros futuros por conta da criação de diretórios já existentes, neste caso os diretórios `vendas` e `backup`. 
- É importante ressaltar a utilização dos caminhos absolutos no script. Na Seção 7 este tema será mais abordado, pois foi uma das maiores dificuldades encontradas na realização deste código.

![imagem_02](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/evidencias/02_codigo_criacao_subdiretorios.png) 

Abaixo, podemos ver o resultado desta primeira parte do script. Nota-se a utilização do `chmod u+x` para garantir a permissão de execução do arquivo. 

![imagem_03](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/evidencias/03_resultado_codigo_criacao_subdiretorios.png) 

### 3.2 Renomeação do arquivo de backup

Para a renomeação do arquivo `dados_de_vendas.csv`, foi necessário a definição da variável `data` conforme a data atual do sistema operacional. Com o comando `data=$(date +%Y%m%d)` é possível obter este resultado. Assim, bastou realizar a cópia do arquivo para a pasta `backup` e a renomeação do arquivo com o comando `mv`.

```bash
data=$(date +%Y%m%d)
cp dados_de_vendas.csv /home/heitorkobayashi/ecommerce/vendas/backup
cd /home/heitorkobayashi/ecommerce/vendas/backup
mv dados_de_vendas.csv backup-dados-$data.csv
```

- Nota-se a utilização do `$`, que junto do `=` foi utilizado para atribuir valores a variáveis e substituir valores, como no caso da renomeação do arquivo de `backup` com a data atual do sistema.

### 3.3 Extração de dados

Para extrair as informações do arquivo `.csv`, foi necessário armazenar o nome do arquivo de backup renomeado em uma variável, no caso, com toda a criatividade disponível no momento, a variável `dados_tabela`, possibilitando o acesso ao arquivo. 

```bash
dados_tabela="backup-dados-$data.csv"
primeiro_registro=$(awk -F ',' 'NR==2 {print $5}' "$dados_tabela")
ultimo_registro=$(awk -F ',' 'END {print $5}' "$dados_tabela")
total_itens=$(awk 'NR!=1' "$dados_tabela" | wc -l)
```

Para cada item de informação contida no relatório foram definidas variáveis, como o "primeiro registro de vendas", o "último registro de vendas" e a "quantidade total de itens diferentes". Dessa forma, além de facilitar na parte do código da criação do relatório, foi possível armazenar os dados solicitados e extraí-los utilizando o comando `awk`, que se deu por vários motivos:

- O comando `awk` foi projetado para trabalhar com dados estruturados por colunas, ou seja, muito útil para arquivos `.csv`.
- Além disso, ele processa o arquivo linha por linha, o que era exatamente o necessário nessa situação.
- A flag `-F` é extremamente útil para delimitar os campos, neste caso, a vírgula.

Agora, sobre os demais itens da sintaxe:

- O comando `NR` é um contador automático de linhas, dessa forma, ele define a linha pretendida, sendo possível acessar as linhas desejadas.
- O comando `{print $5}` define a impressão do quinto campo da linha.
- O comando `END` faz com que a ação do `awk` seja contabilizada até a última linha, poupando o trabalho de fazer a contagem com `NR`.
- Para a variável `total_itens`, foi levado em consideração apenas a extração de todos os itens, não importando o id dos itens e o cabeçalho. Para isso, foi necessário a utilização do `NR!=1` para ignorar a primeira linha e a utilização do `wc -l`, para contar o restante das linhas.
- O comando `wc` é utilizado para contar linhas e caracteres. Com a flag `-l`, define a contagem apenas das linhas. Dessa forma é possível contabilizar o número total de itens.
- O `|` se chama pipe, um operador que permite conectar as entradas e saídas dos comandos.

### 3.4 Criação do arquivo relatorio.txt

Para a criação do arquivo `relatorio.txt` foi utilizado a atribuição da variável `arquivo` ao nome do arquivo de relatório que será criado.

```bash
arquivo="relatorio-$data.txt"
```

- Nota-se a utilização da variável `$data` para atribuição do nome ao arquivo conforme solicitado.

Agora, para que o relatório pudesse conter todas as informações que foram extraídas, foi utilizado o comando `cat`. Aqui, farei uma breve pausa para explicar a minha linha de raciocínio nessa escolha:

- Durante as minhas pesquisas sobre como eu poderia colocar os dados extraídos dentro de um arquivo, eu vi diversos comandos para fazer isso, como o `echo`, `printf` e até mesmo o `awk`. Mas esses métodos não estavam fazendo muito sentido para mim. Vendo as aulas de linux lembrei do comando `cat xarquivo.txt >> yarquivo.txt` que é capaz de concatenar o conteúdo de um arquivo dentro de outro arquivo. Dessa forma, fui atrás para saber se existia algum jeito de fazer isso utilizando o `cat`. E não é que era possível? Depois de muita pesquisa, achei esse notação:

    ```bash
    cat << END > "arquivo" 
    texto
    END
    ```
    A sintaxe utilizada por este comando é muito semelhante ao pouco que sei de programação, assim consegui assimilar a algo que já conhecia previamente, facilitando a minha vida e o andamento do desafio.

Voltando ao que interessa, a escolha pelo pelo `cat` também foi motivada por outros fatores:

- A facilidade de usar, o comando é muito intuitivo, de fácil leitura e possibilita a utilização de vários blocos de textos no próprio corpo do comando.
- Com ele é possível inserir as variáveis que foram definidas anteriormente de forma simples. 


```bash
arquivo="relatorio-$data.txt"
cat << END > "$arquivo"
Data do primeiro registro: $primeiro_registro
Data do último registro: $ultimo_registro
Total de itens: $total_itens
Data e hora da geração do relatório: $(date +'%Y%m%d %Hh:%Mm')
$(tail -n +2 backup-dados-$data.csv | head -n 10)
END
```
Acima, podemos ver o comando completo e ressaltar alguns pontos:

- O conteúdo que será escrito no relatório está entre `<< END` e `END`. Como dito anteriormente, as variáveis podem ser adicionadas ao corpo do texto, facilitando a leitura.
- A inclusão das horas e minutos na definição da data. 
- A utilização do comando `tail` e `head` para extrair do arquivo apenas os 10 primeiros itens da lista. Lembrando que a flag `-n` define exatamente a linha a ser delimitada.

Na imagem abaixo, podemos conferir todo o procedimento realizado: 

![imagem_04](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/evidencias/04_codigo_extracao_dados_criacao_relatorio.png) 

Para notificar o usuário de que o relatório foi gerado com sucesso, o comando `echo` foi utilizado, assim como o comando `cat` para facilitar a visualização e ter a certeza de que o relatório estava conforme o solicitado, como mostra o resultado do script na imagem abaixo:

![imagem_05](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/evidencias/05_resultado_extracao_dados_criacao_relatorio.png)

### 3.5 Compressão do arquivo em zip e remoção dos arquivos `.csv`

Com o `zip` instalado no sistema, pode-se realizar a compressão do arquivo de backup e, posteriormente, a remoção dos arquivos `.csv`, conforme a imagem abaixo:

![imagem_06](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/evidencias/06_zip_remocao_backup.png)

A utilização do `zip -r` foi essencial para incluir todos os arquivos e subdiretórios dentro do diretório desejado: Ou melhor, utilizando os jargões técnicos, de forma recursiva (coisas que aprendemos na prática... por muitas tentativas o meu zip deu errado).

## 4. Criação do Script 2


## 5. Execução do Processamento

## 6. Resultados

## 7. Dificuldades Durante o Desafio

## 8. Considerações Finais

## 9. Referências
