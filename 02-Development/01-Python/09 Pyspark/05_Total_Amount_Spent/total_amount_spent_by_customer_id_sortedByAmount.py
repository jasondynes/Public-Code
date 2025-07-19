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

customersByTotal = rdd.reduceByKey(add)
sortedByAmount = customersByTotal.map(lambda x: (x[1], x[0])).sortByKey()

totals_results = sortedByAmount.collect()

for total in totals_results:
    print(round(total[0],2),total[1])

