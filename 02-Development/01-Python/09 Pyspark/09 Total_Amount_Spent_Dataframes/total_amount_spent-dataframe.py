from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

spark = SparkSession.builder.appName("total_amount_spent").getOrCreate()

schema = StructType([ \
                     StructField("customerId", IntegerType(), False), \
                     StructField("itemId", IntegerType(), False), \
                     StructField("amount_spent", FloatType(), False)])

# // Read the file as dataframe
df = spark.read.schema(schema).csv("file:///SparkCourse/customer-orders.csv")
# Show the schema of the dataframe
df.printSchema()
# Group by customerId and sum the amount_spent for each customer
total_spent_df = df.groupBy("customerId").agg(func.round(func.sum("amount_spent"), 2).alias("total_spent")).sort("total_spent", ascending=False)
# Show the results.
total_spent_df.show(total_spent_df.count())
# Stop the Spark session
spark.stop()

                                                  