import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, input_file_name, col
from datetime import datetime


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])


spark = SparkSession.builder \
    .appName("Processo_json_Trustedzone") \
    .getOrCreate()


raw_path = args['S3_INPUT_PATH']
trusted_path = f"{args['S3_TARGET_PATH']}/API"


raw_df = spark.read.option("multiline", "true").json(raw_path)
current_date = datetime.now()
raw_df = raw_df.withColumn("year", lit(current_date.year)) \
               .withColumn("month", lit(f"{current_date.month:02}")) \
               .withColumn("day", lit(f"{current_date.day:02}"))
               
for year, month, day in raw_df.select("year", "month", "day").distinct().collect():
    partitioned_df = raw_df.filter((col("year") == year) & (col("month") == month) & (col("day") == day))
    path = f"{trusted_path}/{year}/{month}/{day}"
    partitioned_df.write.mode("overwrite").parquet(path)
            
print("Processamento do .json concluído!")
spark.stop()


sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
job.commit()