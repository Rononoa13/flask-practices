from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def roll_dice():
    random_number = randint(1, 6)
    return f"The dice rolled: {random_number}"
