from pyspark.sql import SparkSession
import re

sessao_spark = SparkSession.builder.appName("ContagemPalavrasMarkdown").getOrCreate()

arquivo_texto = sessao_spark.read.text("README.md")

palavras = arquivo_texto.rdd.flatMap(lambda linha: re.split(r"\W+", linha[0].lower()))
contagem_palavras = palavras.filter(lambda palavra: palavra != "").map(lambda palavra: (palavra, 1)).reduceByKey(lambda a, b: a + b)

for palavra, contagem in contagem_palavras.collect():
    print(f"{palavra}: {contagem}")
    