import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, year, month, dayofmonth, monotonically_increasing_id, explode, floor

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'REFINED_PATH', 'STAGING_PATH'])

refined_path = f"{args['REFINED_PATH']}"
staging_path = args['STAGING_PATH']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

staging_df = spark.read.parquet(staging_path)
staging_df = staging_df.dropna(subset=[
    "idfilmes", "title", "release_date", "origin_country", 
    "original_language", "vote_average", "vote_count", 
    "popularity", "budget", "revenue", "runtime"
])
staging_df_exploded = staging_df.withColumn("pais", explode(col("origin_country")))

dim_filme = staging_df_exploded.select(
    col("idfilmes").cast("string").alias("idFilme"),
    col("title").cast("string").alias("titulo")
).dropDuplicates()
dim_filme.write.mode("overwrite").parquet(f"{refined_path}/dim_filme")

dim_tempo = staging_df_exploded.select(
    col("release_date").cast("date").alias("data_estreia"),
    year(col("release_date")).cast("int").alias("ano"),
    month(col("release_date")).cast("int").alias("mes"),
    dayofmonth(col("release_date")).cast("int").alias("dia"),
    (floor((month(col("release_date")) - 1) / 3) + 1).cast("int").alias("trimestre")
).withColumn("idTempo", monotonically_increasing_id()).dropDuplicates()
dim_tempo.write.mode("overwrite").parquet(f"{refined_path}/dim_tempo")

dim_localizacao_casted = staging_df_exploded.select(
    col("pais").cast("string").alias("pais"),
    col("original_language").cast("string").alias("idioma")
).withColumn("idLocalizacao", monotonically_increasing_id()).dropDuplicates()
dim_localizacao_casted.write.mode("overwrite").parquet(f"{refined_path}/dim_localizacao")

fato_filmes = staging_df_exploded.withColumnRenamed("idfilmes", "idFilme").join(
    dim_filme.select(col("idFilme")),
    on="idFilme",
    how="inner"
).join(
    dim_tempo.select(col("idTempo"), col("data_estreia")),
    on=staging_df_exploded["release_date"] == dim_tempo["data_estreia"],
    how="inner"
).join(
    dim_localizacao_casted.select(col("idLocalizacao"), col("pais"), col("idioma")), 
    on=[staging_df_exploded["pais"] == dim_localizacao_casted["pais"],
    staging_df_exploded["original_language"] == dim_localizacao_casted["idioma"]], 
    how="inner"
)

fato_filmes = fato_filmes.withColumn("idFilme", col("idFilme").cast("string"))

fato_filmes = fato_filmes.select(
    col("idFilme"),
    col("idTempo"),
    col("idLocalizacao"),
    col("budget").cast("bigint").alias("orcamento"),
    col("revenue").cast("bigint").alias("receita"),
    col("runtime").cast("bigint").alias("duracao"),
    col("vote_average").cast("double").alias("avaliacao_media"),
    col("vote_count").cast("bigint").alias("votos_totais"),
    col("popularity").cast("double").alias("popularidade")
).dropDuplicates()

fato_filmes.write.mode("overwrite").parquet(f"{refined_path}/fato_filmes")

print(f"Processamento concluído. Tabelas criadas e salvas na camada refined.")

job.commit()
