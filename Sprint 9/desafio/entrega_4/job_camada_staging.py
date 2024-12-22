import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col, current_date, date_format, regexp_replace
from datetime import date


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'TRUSTED_PATH_API', 'TRUSTED_PATH_CSV', 'STAGING_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


trusted_api_path = args['TRUSTED_PATH_API']
trusted_csv_path = args['TRUSTED_PATH_CSV']
staging_base_path = f"{args['STAGING_PATH']}/Staging/Parquet"


api_df = spark.read.parquet(trusted_api_path)
csv_df = spark.read.parquet(trusted_csv_path)


api_df = api_df.select(
    "budget", "imdb_id", "origin_country", "original_language",
    "title", "popularity", "release_date", "revenue",
    "vote_average", "vote_count", "runtime", "genres"
)

csv_df = csv_df.select(
    "id", "notamedia", "numerovotos", "genero", "anolancamento"
)

api_df = api_df.filter(col("budget").isNotNull() & (col("budget") >= 0))
api_df_colunas = (
    api_df.withColumn("idFilmes", regexp_replace(col("imdb_id"), "^tt", ""))
    .drop("imdb_id")
)


csv_df_colunas = (
    csv_df.withColumn("idFilmes", regexp_replace(col("id"), "^tt", ""))
    .drop("id")
)

staging_df = api_df_colunas.unionByName(csv_df_colunas, allowMissingColumns=True)
staging_df = staging_df.dropDuplicates(["idFilmes"])
data_atual = date.today()
dia = data_atual.strftime('%d')
mes = data_atual.strftime('%m')
ano = data_atual.strftime('%y')
custom_path = f"{staging_base_path}/{dia}/{mes}/{ano}"
staging_df.write.mode("overwrite").parquet(custom_path)

print(f"Processamento concluído. Dados armazenados no caminho: {custom_path}")

job.commit()
