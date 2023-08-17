from flask import Flask
from random import randint
app = Flask(__name__)

random_num = 0


@app.route('/')
def hello():
    global random_num
    random_num = randint(0, 9)
    return ('<h2>Guess a number between 0 and 9</h2>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img>')


@app.route('/<int:number>')
def check_num(number):
    if number == random_num:
        return ('<h2>You Guessed It Right!!</h2>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></img>')
    if number > random_num:
        return ('<h2>Too High, Try Again!</h2>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></img>')
    if number < random_num:
        return ('<h2>Too Low, Try Again!</h2>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></img>')


if __name__ == "__main__":
    app.run(debug=True)