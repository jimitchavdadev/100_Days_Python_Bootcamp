from flask import Flask
import random

app = Flask(__name__)

# Generate a random number between 0 and 9
random_number = random.randint(0, 9)

@app.route('/')
def home():
    return '''
    <h1 style="text-align: center;">Guess a number between 0 and 9</h1>
    <p style="text-align: center;"><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="300"></p>
    '''

@app.route('/<int:guess>')
def guess_number(guess):
    if guess < random_number:
        return '''
        <h1 style="color: blue; text-align: center;">Too low! Try again.</h1>
        <p style="text-align: center;"><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="300"></p>
        '''
    elif guess > random_number:
        return '''
        <h1 style="color: red; text-align: center;">Too high! Try again.</h1>
        <p style="text-align: center;"><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="300"></p>
        '''
    else:
        return '''
        <h1 style="color: green; text-align: center;">You found me!</h1>
        <p style="text-align: center;"><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="300"></p>
        '''

if __name__ == "__main__":
    app.run(debug=True)
