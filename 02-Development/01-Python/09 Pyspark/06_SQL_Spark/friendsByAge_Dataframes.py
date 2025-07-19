from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions as func

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

lines = spark.read.option("header", "true").option("inferSchema", "true")\
    .csv("file:///SparkCourse/fakefriends-header.csv")
    
# Select only age and numFriends columns
friendsByAge = lines.select("age", "friends")
friendsByAge.groupBy("age").agg(func.round(func.avg("friends"), 2)).orderBy("age", ascending=True).show()

spark.stop()