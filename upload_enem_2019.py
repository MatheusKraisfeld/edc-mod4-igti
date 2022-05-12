import os
import pyspark
from pyspark.sql import SparkSession

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

spark = (
    SparkSession.builder.config("spark.hadoop.fs.s3a.access.key", AWS_ACCESS_KEY_ID)
    .config("spark.hadoop.fs.s3a.secret.key", AWS_SECRET_ACCESS_KEY)
    .config("spark.driver.memory", "12g")
    .config("spark.executor.memory", "12g")
    .config("spark.hadoop.fs.s3a.fast.upload", True)
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.1.2,io.delta:delta-core_2.12:1.0.0")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.hadoop.fs.s3a.bucket.all.committer.magic.enabled", "true")
    .config("spark.debug.maxToStringFields", "100")
    .getOrCreate()
)
spark._jsc.hadoopConfiguration().set(
    "fs.s3a.aws.credentials.provider",
    "com.amazonaws.auth.InstanceProfileCredentialsProvider,com.amazonaws.auth.DefaultAWSCredentialsProviderChain",
)

df = (
    spark.read.option("inferSchema", "true")
    .option("delimiter", ";")
    .option("header", "true")
    .csv(
        "/mnt/e/Estudos/ENEM_2019/DADOS/MICRODADOS_ENEM_2019.csv"
    )
)
df.printSchema()
# df.write.mode("overwrite").partitionBy("TP_ANO_CONCLUIU").csv(
#     "s3a://datalake-kraisfeld-igti-edc/staging/enem/"
# )

# df.write.mode("overwrite").option('header', 'true').csv(
#     "s3a://landing-zone-741358071637/enem/year=2019"
# )

df.write.mode("overwrite").parquet(
    "s3a://landing-zone-741358071637/enem/2019"
)