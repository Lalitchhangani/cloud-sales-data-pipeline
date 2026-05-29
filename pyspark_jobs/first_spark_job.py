import os

os.environ["JAVA_HOME"] = r"C:\Program Files\Eclipse Adoptium\jdk-17.0.19.10-hotspot"

from pyspark.sql import SparkSession

print("Starting Spark...")

spark = SparkSession.builder \
    .appName("MyFirstSparkJob") \
    .master("local[*]") \
    .getOrCreate()

print("Spark Started Successfully")

spark.stop()

print("Spark Stopped")