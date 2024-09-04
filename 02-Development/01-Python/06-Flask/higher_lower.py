from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def main_page():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"</img src>')


random_num = random.randint(0, 9)


@app.route("/<int:guess>")
def num_guess(guess):
    if random_num == guess:
        message = ('<h1 style="color: purple">you guessed correctly</h1>'
                   '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"</img src>')
    elif random_num < guess:
        message = '<h1 style="color: red">you guessed too high</h1><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"</img src>'
    else:
        message = ('<h1 style="color: green">you guessed too low</h1>'
                   '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"</img src>')
    return message


app.run(debug=True)
