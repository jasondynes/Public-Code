from pyspark import SparkConf, SparkContext
from operator import add

conf = SparkConf().setMaster("local").setAppName("total_amount_spent_by_customer")
sc = SparkContext(conf = conf)


def parseLine(line):
    fields = line.split(',')
    customer_id = int(fields[0])
    amount_spent = float(fields[2])
    return (customer_id, amount_spent)

lines = sc.textFile("file:///SparkCourse/customer-orders.csv")
rdd = lines.map(parseLine)

customersByTotal = rdd.reduceByKey(add).sortByKey()

totals_results = customersByTotal.collect()

for total in totals_results:
    print(total[0], round(total[1],2))

