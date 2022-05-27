import pandas
gray_count = 0
red_count = 0
black_count = 0


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

for col in data["Primary Fur Color"]:
    if col == "Gray":
        gray_count+=1
    elif col=='Cinnamon':
        red_count+=1
    elif col=='Black':
        black_count += 1

fur_colors = {
    "Fur Color": ['Gray', 'Red', 'Black'],
    "Count": [gray_count, red_count, black_count]
}
fur_colors_data=pandas.DataFrame(fur_colors)
fur_colors_data.to_csv("Fur_colors.csv")
