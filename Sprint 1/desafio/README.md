# **Sprint 1: Desafio**

## 1. Objetivos

Este desafio teve como objetivo a criação de dois scripts que automatizassem a geração de relatórios de vendas a partir de um arquivo `.cvs`.

O primeiro script, o qual chamaremos de [Script 1](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/desafio/entregaveis/ecommerce/processamento_de_vendas.sh), realizava a criação de diretórios e subdiretórios, copia Já o segundo script, [Script 2](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/desafio/entregaveis/ecommerce/consolidador_de_processamento_de_vendas.sh), teve como função a junção de todos os relatórios gerados a partir do script anterior e, assim, criar um arquivo chamado `relatorio_final.txt`
## 2. Preparação

Antes de iniciarmos o script em si, foi necessário a preparação da nossa área de trabalho, ou seja, a criação dos diretórios necessários para realização deste desafio.

### 2. 1. Criação do diretório ecommerce

Para criar o diretório `ecommerce` foi utilizado o comando `mkdir ecommerce`. O arquivo `dados_de_vendas.csv` foi inserido manualmente no linux. Com o comando `ls` podemos listar os diretórios e arquivos existentes, como mostra a imagem abaixo:

![imagem_01](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/evidencias/01_criacao_pasta_ecommerce.png) 


## 3. Criação do Script 1

Nesta etapa, Dei preferência por criar em etapas, para ter certeza de que estava indo pelo caminho correto e não deixar para ter surpresas no fim do código

### 3.1 Criação dos subdiretórios

O primeiro passo desse script foi a criação dos subdiretórios `vendas` e `backup`, além da realização de uma cópia do arquivo `dados_de_vendas.csv` para a pasta `vendas`.

- Com o comando `cd` definimos onde o script será executado.
- Sabendo que o script será realizado mais que uma vez, com o `mkdir -p` podemos realizar a criação da pasta vendas e prevenir erros futuros por conta da criação de diretórios já existentes, neste caso os diretórios `vendas` e `backup`. 
- É importante ressaltar a utilização dos caminhos absolutos no script. Na Seção 7 irei abordar mais sobre este tema, pois foi uma das maiores dificuldades que tive na realização deste código.

![imagem_02](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/evidencias/02_codigo_criacao_subdiretorios.png) 

Abaixo, podemos ver o resultado desta primeira parte do script. Nota-se a utilização do `chmod u+x` para garantir a permissão de execução do arquivo. 

![imagem_03](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/evidencias/03_resultado_codigo_criacao_subdiretorios.png) 

### 3.2 Renomeação do arquivo de backup

Para a renomeação do arquivo `dados_de_vendas.csv`, foi necessário a definição da variável `data` conforme a data atual do sistema operacional. Dessa forma, `data=$(date +%Y%m%d)`. Assim, bastou realizar a cópia do arquivo para a pasta `backup` e a renomeação do arquivo com o comando `mv`.

```bash
data=$(date +%Y%m%d)
cp dados_de_vendas.csv /home/heitorkobayashi/ecommerce/vendas/backup
cd /home/heitorkobayashi/ecommerce/vendas/backup
mv dados_de_vendas.csv backup-dados-$data.csv
```

### 3.3 Extração de dados

```bash
dados_tabela="backup-dados-$data.csv"
```
```bash
primeiro_registro=$(awk -F ',' 'NR==2 {print $5}' "$dados_tabela")
ultimo_registro=$(awk -F ',' 'END {print $5}' "$dados_tabela")
total_itens=$(awk 'NR!=1' "$dados_tabela" | wc -l)
```

### 3.4 Criação do arquivo relatorio.txt

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

Na imagem abaixo, podemos conferir todo o procedimento realizado: 

![imagem_04](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/evidencias/04_codigo_extracao_dados_criacao_relatorio.png) 

Essa parte do script foi finalizada com uma mensagem a partir do comando `echo` para notificar o usuário que o relatório foi gerado com sucesso. Utilizei o comando `cat` para facilitar a visualização e ter a certeza de que o relatório estava conforme o solicitado, como mostra a imagem abaixo:

![imagem_05](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%201/evidencias/05_resultado_extracao_dados_criacao_relatorio.png)

### 3.5 Compressão do arquivo em zip e remoção dos arquivos `.csv`




## 4. Criação do Script 2


## 5. Execução do Processamento

## 6. Resultados

## 7. Dificuldades Durante o Desafio

## 8. Considerações Finais
