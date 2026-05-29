import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

os.environ["JAVA_HOME"] = r"C:\Program Files\Eclipse Adoptium\jdk-17.0.19.10-hotspot"

spark = SparkSession.builder \
    .appName("ReadSalesCSV") \
    .master("local[*]") \
    .getOrCreate()

# Read CSV
df = spark.read.csv(
    "data/sales.csv",
    header=True,
    inferSchema=True
)

print("Sales Data using PySpark")
df.show()

print("Schema")
df.printSchema()

# Transformation
customer_sales = df.groupBy("customer") \
                   .agg(sum("amount").alias("total_sales"))

print("Customer Sales")
customer_sales.show()

customer_sales.toPandas().to_csv(
    "data/customer_sales_spark.csv",
    index=False
)

print("Output Saved Successfully")

print("Output Saved Successfully")

spark.stop()