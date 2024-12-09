import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import input_file_name
from datetime import datetime
    

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])
    
    
spark = SparkSession.builder \
    .appName("Processo_csv_Trustedzone") \
    .getOrCreate()
    
    
raw_path = args['S3_INPUT_PATH']
trusted_path = f"{args['S3_TARGET_PATH']}/CSV"
    
    
raw_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .option("delimiter", "|") \
    .csv(raw_path)

current_date = datetime.now()
year = current_date.year
month = f"{current_date.month:02d}"
day = f"{current_date.day:02d}"

partitioned_path = f"{trusted_path}/{year}/{month}/{day}"
raw_df.write.mode("overwrite").parquet(partitioned_path)
print("Processamento do .csv concluído!")
spark.stop()
    
    
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
job.commit()
