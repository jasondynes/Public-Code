# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#     data.pop(0)
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["day"])
# print(data["temp"])
# print(data["condition"])
# print(f"\n{data}")
#
# data_dict = data.to_dict()
# print(f" \n\n****************************\n data converted to a dictionary\n ****************************\n {data_dict}")
#
# print(f"\n\n convert a column (pandas series) to a list")
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print("calculate the average temperature using standard python")
# avg_temp = round(sum(temp_list) / len(temp_list), 2)
# print(f"average temperature in list is {avg_temp}")
#
#
# print("\n\ncalculate the average temperature using Pandas")
# avg_temp = round(data["temp"].mean(), 2)
# print(f"average temperature in list is {avg_temp} using MEAN method in Pandas")
# # calculation in f string
# print(f'average temperature in list is {round(data["temp"].mean(), 2)} using MEAN method in Pandas')
#
#
# print("\n\ncalculate the maximum temperature using Pandas")
# max_temp = round(data["temp"].max(), 2)
# print(f"maximum temperature in list is {max_temp} using MAX method in Pandas")
# # calculation in f string also using :.2f for 2dp float
# print(f'maximum temperature in list is {data["temp"].max():.2f} using MAX method in Pandas')
# print("\ndata.temp used instead of data['temp'']")
# print(f'maximum temperature in list is {data.temp.max():.2f} using MAX method in Pandas')
#
# print("Get a row with pandas")
# print(data[data.day == "Monday"])
#
# print("Get a row with pandas showing day where temperature is max")
# print(data.day[data.temp == data.temp.max()])

# print("Get Monday's temperature and covert to deg C from Celsius")
# monday_temp = (data.temp[data.day == "Monday"])
# monday_temp_F = (monday_temp * 9/5 + 32)
#
# print(f"Monday's temperature was {monday_temp_F} in deg F")
# print(monday_temp_F)
# print(data.temp[data.day == "Monday"])
#
# print(data)
data_dict = {
    "students": ["Ethan", "Jason", "Roxana"],
    "scores": [54, 56, 60],
}
data = pandas.DataFrame(data_dict)
print(data)
# output to CSV file
data.to_csv("new_file.csv")