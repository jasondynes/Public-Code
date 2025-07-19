from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

people = spark.read.option("header", "true").option("inferSchema", "true")\
    .csv("file:///SparkCourse/fakefriends-header.csv")
    
print("Here is our inferred schema:")
people.printSchema()

print("Let's display the name column:")
people.select("name").show()

print("Filter out anyone 21 or over:")
people.filter(people.age < 21).show()

print("Group by age")
# people.groupBy("age").count().show()
# sorted by age - use orderBy method
people.groupBy("age").count().orderBy("age", ascending=True).show()


print("Make everyone 10 years older:")
people.select(people.name, people.age + 10).show()

spark.stop()

