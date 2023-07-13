import turtle
import pandas

# def avgOfList(list):
#     return sum(list)/len(list)

# data = pandas.read_csv("Day25/weather_data.csv")
# # data_list = data["temp"].to_list()
# # print(avgOfList(data_list))

# monday = data[data.day == "Monday"]
# temp = (monday.temp*9/5)+32
# print(f"{temp} F")

# data = pandas.read_csv("Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
# gray = len(data[data["Primary Fur Color"] == "Gray"])
# black = len(data[data["Primary Fur Color"] == "Black"])

# print(f"Count of CinnamonSq is : {cinnamon}")
# print(f"Count of GraySq is : {gray}")
# print(f"Count of BlackSq is : {black}")

# data_dict = {
#     "Fur Color" : ["Gray", "Cinnamon", "Black"],
#     "Count" : [gray, cinnamon, black]
# }

# df = pandas.DataFrame(data_dict)
# df.to_csv("Day25/squirel_colors.csv")

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    ans_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state's name?").title()

    if ans_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("StatestoLearn.csv")
        break
    if ans_state in all_states:
        guessed_states.append(ans_state)
        t = turtle.Turtle()
        turtle.hideturtle()
        t.penup()
        state_data = data[data["state"] == ans_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(ans_state)

screen.exitonclick()
