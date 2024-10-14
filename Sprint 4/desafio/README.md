# **Sprint 4: Desafio**

## **1. Objetivos**

Este desafio teve como objetivo a prática de Docker utilizando técnicas para a criação de imagens e execução de containers. 

Ao todo, foram 3 etapas. A primeira solicitava a construção de uma imagem que executasse o código disponibilizado `carguru.py` para poder executar o container a partir dessa imagem. A segunda etapa consistia em responder se é possível a reutilização de containers. Por fim, a terceira etapa requisitava um exercício de criação de container que permitia receber inputs durante a execução a partir da criação de um script em Python.

Clique nos seguintes links para acessar os respectivos códigos:

- [Dockerfile - Etapa 1](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%204/desafio/etapa_1/Dockerfile)
- [Código "Carguru.py" - Etapa 1](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%204/desafio/etapa_1/carguru.py)
- [Dockerfile - Etapa 3](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%204/desafio/etapa_3/Dockerfile)
- [Script - Etapa 3](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%204/desafio/etapa_3/script_etapa_3.py)

## **2. Preparação**

Para a resolução do desafio, foi necessário a preparação do ambiente, ou seja, o download e instalação do Docker, que correu sem maiores problemas. 

## **3. Desenvolvimento**

### **3.1. Etapa 1**

Como dito anteriormente, a primeira estapa solicitava a construção de uma imagem que executasse o código disponibilizado `carguru.py` para poder executar o container a partir dessa imagem. Na imagem abaixo, podemos ver a construção da imagem `desafio-etapa1`.

![imagem_01](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%204/evidencias/imagem_desafio_01.png)

Na sequência, podemos ver a execução do container:

![imagem_02](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%204/evidencias/imagem_desafio_02.png)


### **3.2. Etapa 2**

É possível reutilizar um container? Sim, é possível. Para comprovar isso, foi feito o seguinte exercício:

![imagem_06](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%204/evidencias/imagem_desafio_06.png)

- Após realizado todas as atividades do desafio, essas eram as imagens listadas. Com um simples comando `docker start` foi possível reutilizar os containers que constam na imagem acima. A flag `-i` foi utilizada para manter o modo interativo, dessa forma permitindo interação com o container diretamente, o que era necessário para as respectivas imagens.

### **3.3. Etapa 3**

Para a terceira etapa, foi requesitado a criação uma imagem chamada `mascarar-dados` para a execução de um script Python. 

Esse script é capaz de gerar um hash a partir de um input de uma string. Confeço que essa foi, de longe, a parte mais complicada do desafio, pois nunca havia trabalhados com esse tipo de algoritmo. 

Apesar disso, o script é simples e você pode conferir [aqui](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%204/desafio/etapa_3/script_etapa_3.py). Foi necessário importar a biblioteca `hashlib` e a partir disso, com uma simples iteração, gerar a hash a partir de um input.

Na imagem abaixo, é possível ver a criação da imagem:

![imagem_03](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%204/evidencias/imagem_desafio_03.png)

E agora, o container em execução:

![imagem_04](https://github.com/heitorkobayashi/PB-HEITOR-KOBAYASHI/blob/main/Sprint%204/evidencias/imagem_desafio_04.png)


## **4. Considerações finais**

Durante o desenvolvimento deste desafio não enfrentei dificuldades. A parte mais complicada foi a criação do script da terceira etapa, pois nunca tinha trabalhado com algoritmos _SHA_ e _hashs_, então precisou ser feito uma breve pesquisa sobre esses algoritmos de segurança e suas aplicações. 

## **5. Referências**

- BRILLIANT. **Secure Hashing Algorithms (SHA)**. Disponível em: https://brilliant.org/wiki/secure-hashing-algorithms/. Acesso em: 5 out. 2024.

- NEURALNINE. **Hashing in Python: Using Hashlib Library for Secure Hashing**. Disponível em: https://www.youtube.com/watch?v=i-h0CtKde6w. Acesso em: 5 out. 2024.
