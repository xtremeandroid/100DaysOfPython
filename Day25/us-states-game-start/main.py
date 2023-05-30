import turtle

screen = turtle.Screen()
screen.title("US States Game")

image = "Day25/us-states-game-start/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

answer_state=screen.textinput("Guess The State", "What's another state's name? ")


screen.exitonclick()

