import os

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

aws_access_key_id = os.environ["AWS_ACCESS_KEY_ID"]
aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]

# set conf
conf = (
    SparkConf()
    .set("spark.hadoop.fs.s3a.access.key", aws_access_key_id)
    .set("spark.hadoop.fs.s3a.secret.key", aws_secret_access_key)
    .set("spark.hadoop.fs.s3a.fast.upload", True)
    .set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    .set("fs.s3a.endpoint", "s3.us-east-2.amazonaws.com")
    .set("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.2.0")
    .set("spark.jars.repositories", "https://repos.spark-packages.org")
)
print('********** Conf **********')
# apply config
sc = SparkContext(conf=conf).getOrCreate()
sc.setSystemProperty("com.amazonaws.services.s3.enableV4", "true")
sc._jsc.hadoopConfiguration().set("com.amazonaws.services.s3.enableV4", "true").set(
    "fs.s3a.endpoint", "s3.us-east-2.amazonaws.com"
)

if __name__ == "__main__":

    # init spark session
    spark = SparkSession.builder.appName("Repartition Job").getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    df = (
        spark.read.format("csv")
        .options(header="true", inferSchema="true", delimiter=";")
        .load("s3a://datalake-kraisfeld-igti-edc/raw-data/titanic/titanic.csv")
    )

    df.show()
    df.printSchema()

    (
        df.write.mode("overwrite")
        .format("parquet")
        .save("s3a://datalake-kraisfeld-igti-edc/staging/titanic")
    )

    print("*****************")
    print("Escrito com sucesso!")
    print("*****************")

    spark.stop()
