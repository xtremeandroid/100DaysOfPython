import pandas

# def avgOfList(list):
#     return sum(list)/len(list)

# data = pandas.read_csv("Day25/weather_data.csv")
# # data_list = data["temp"].to_list()
# # print(avgOfList(data_list))

# monday = data[data.day == "Monday"]
# temp = (monday.temp*9/5)+32
# print(f"{temp} F")

data = pandas.read_csv("Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])

print(f"Count of CinnamonSq is : {cinnamon}")
print(f"Count of GraySq is : {gray}")
print(f"Count of BlackSq is : {black}")

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray, cinnamon, black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Day25/squirel_colors.csv")
