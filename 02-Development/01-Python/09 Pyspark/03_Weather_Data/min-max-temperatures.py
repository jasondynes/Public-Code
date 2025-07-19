from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    stationID = fields[0]
    entryType = fields[2]
    temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0
    return (stationID, entryType, temperature)

lines = sc.textFile("file:///SparkCourse/1800.csv")
parsedLines = lines.map(parseLine)

Temps = parsedLines.filter(lambda x: x[1] in ("TMIN", "TMAX"))

stationTemps = Temps.map(lambda x: (x[0], x[2]))

minTemps = stationTemps.reduceByKey(lambda x, y: min(x,y))
maxTemps = stationTemps.reduceByKey(lambda x, y: max(x,y))

min_results = minTemps.collect();
max_results = maxTemps.collect();

for result in min_results:
    print("Minimum temp " + result[0] + "\t{:.2f}F".format(result[1]))
    
for result in max_results:
    print("Maximum temp " + result[0] + "\t{:.2f}F".format(result[1]))
