from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# A Spark Job to anonymise data
def anonymize_data(input_path, output_path):
    spark = SparkSession.builder.appName("Anonymise Data").getOrCreate()


    df = spark.read.csv(input_path, header=True)

    anonymised_df = df.withColumn("first_name", lit("ANONYMISED")) \
                      .withColumn("last_name", lit("ANONYMISED")) \
                      .withColumn("address", lit("ANONYMISED"))

    anonymised_df.write.mode("overwrite").csv(output_path, header=True)

    spark.stop()

if __name__ == "__main__":
    anonymize_data('data.csv', 'anonymised_data.csv')