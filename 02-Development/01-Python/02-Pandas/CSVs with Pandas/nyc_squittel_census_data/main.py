# data set used is:
# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/data_preview

import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240520.csv")
# use Pandas to create a count based on 'Primary Fur Color' column
print(squirrel_data['Primary Fur Color'].value_counts(ascending=True))

# alternative is to construct using LENGTH method
grey_squirrels = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
red_squirrels = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])
print(grey_squirrels, red_squirrels, black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}
# create pandas dataframe
print(data_dict)
df = pandas.DataFrame(data_dict)
# output to CSV file
df.to_csv("squirrel_count.csv")
