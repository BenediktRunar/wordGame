from flask import Flask, render_template, url_for
from letters import *
from computersTurn import *

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', title='Home')


@app.route("/twoPlayer")
def TwoPlayer():
    return render_template('twoPlayer.html', title='P vs P')


@app.route("/playerVsComputer")
def playerVsComputer():
    # List of tuples with random letters and their corresponding value
    randLetters = get_rand_english_letters()
    # List of the random letters
    randLettersList = [i[0] for i in randLetters]
    # The random letters in a string
    randLettersString = (''.join(randLettersList)).lower()
    randPcString = computers_turn(randLettersString)

    # Get value of word
    wordScore = score_of_english_word(computers_turn(randPcString))

    return render_template('playerVsComputer.html', l=randLetters, word=randPcString, wordScore=wordScore, title='P vs Ai')


if __name__ == '__main__':
    app.run(debug=True)
