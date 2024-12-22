import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, year, month, dayofmonth, monotonically_increasing_id, lit

## @params: [JOB_NAME, REFINED_PATH, STAGING_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'REFINED_PATH', 'STAGING_PATH'])

refined_path = f"{args['REFINED_PATH']}"
staging_path = args['STAGING_PATH']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

staging_df = spark.read.parquet(staging_path)
staging_df = staging_df.dropna(subset=["idfilmes", "title", "release_date", "origin_country", "original_language", "vote_average", "vote_count", "popularity", "budget", "revenue", "runtime"])


dim_filme = staging_df.select(
    col("idfilmes").alias("idFilme"),
    col("title").alias("titulo"),
    col("budget").alias("orcamento"),
    col("revenue").alias("receita"),
    col("runtime").alias("duracao")
).dropDuplicates()
dim_filme.write.mode("overwrite").parquet(f"{refined_path}/dim_filme")


dim_tempo = staging_df.select(
    col("release_date").alias("data_estreia"),
    year(col("release_date")).alias("ano"),
    month(col("release_date")).alias("mes"),
    dayofmonth(col("release_date")).alias("dia")
).withColumn("idTempo", monotonically_increasing_id()).dropDuplicates()
dim_tempo.write.mode("overwrite").parquet(f"{refined_path}/dim_tempo")


dim_popularidade = staging_df.select(
    col("idfilmes").alias("idFilme"),
    col("vote_average").alias("avaliacao_media"),
    col("vote_count").alias("total_votos"),
    col("popularity").alias("popularidade")
).withColumn("idPopularidade", monotonically_increasing_id()).dropDuplicates()
dim_popularidade.write.mode("overwrite").parquet(f"{refined_path}/dim_popularidade")


dim_localizacao = staging_df.select(
    col("origin_country").alias("pais_origem"),
    col("original_language").alias("idioma")
).withColumn("idLocalizacao", monotonically_increasing_id()).dropDuplicates()
dim_localizacao.write.mode("overwrite").parquet(f"{refined_path}/dim_localizacao")


fato_filmes = staging_df.withColumnRenamed("idfilmes", "idFilme").join(
    dim_filme.select("idFilme"),
    on="idFilme",
    how="inner"
).join(
    dim_tempo.select(col("idTempo"), col("data_estreia")),
    on=staging_df["release_date"] == dim_tempo["data_estreia"],
    how="inner"
).join(
    dim_popularidade.select(col("idPopularidade"), col("idFilme")),
    on="idFilme",
    how="inner"
).join(
    dim_localizacao.select(col("idLocalizacao"), col("pais_origem"), col("idioma")),
    on=[staging_df["origin_country"] == dim_localizacao["pais_origem"],
        staging_df["original_language"] == dim_localizacao["idioma"]],
    how="inner"
)


fato_filmes = fato_filmes.select(
    "idFilme",
    "idPopularidade",
    "idTempo",
    "idLocalizacao"
)
fato_filmes.write.mode("overwrite").parquet(f"{refined_path}/fato_filmes")

print(f"Processamento concluído. Tabelas criadas e salvas na camada refined.")

job.commit()
