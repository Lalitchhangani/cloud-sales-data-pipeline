from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("ReadCSV") \
        .master("local[*]") \
        .getOrCreate()

    csv_path = "path/to/your/file.csv"

    df = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load(csv_path)

    df.printSchema()
    df.show(20, truncate=False)

    spark.stop()

if __name__ == "__main__":
    main()