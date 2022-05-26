# with open("weather_data.csv") as wd:
#     data = wd.readlines()
#     print(data)
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
# print(temperatures)
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].tolist()
print(temp_list)

# calculate avg temp
print(sum(temp_list) / len(temp_list))  # long way
print(data["temp"].mean())  # pandas way
print(data["temp"].max())  # biggest value

# get data in columns
# print(data["condition"])
print(data.day)  # alternative way

# get data in row
print(data[data.day == "Monday"])
# highest temp in row
print("-------Highest temp--------\n", data[data.temp == data.temp.max()])

sunday = data[data.day == "Sunday"]
print(sunday.condition)
sunday_temp = int(sunday.temp)
sunday_temp_F = sunday_temp * 9 / 5 + 32
print("Fahrenheit temp sunday:", sunday_temp_F)

# Create a dataframe from scratch
students_data={
    "students":["Amy","James","Angela"],
    "scores": [76,56,86]
}

new_data=pandas.DataFrame(students_data)
print(new_data)
new_data.to_csv("students_data.csv")