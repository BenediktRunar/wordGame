from flask import Flask, render_template, url_for, request, redirect
from letters import *
from computersTurn import *

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', title='Home')

@app.route("/routingToGame")
def routingToGame():
    language= request.args.get('language')
    game = request.args.get('game')
    if game == "twoPlayer":
        temp = "/twoPlayer?language=" + language 
    else:
        temp = "/playerVsComputer?language=" + language

    return redirect(temp + "&turn=1") 

@app.route("/twoPlayer")
def TwoPlayer():
    return render_template('twoPlayer.html', title='P vs P')


@app.route("/playerVsComputer")
def playerVsComputer():
    language = request.args.get('language')
    turn = request.args.get('turn')
    if turn == '1':
        turn = '2'
    else:
        turn = '1'
    print(turn)
    # List of tuples with random letters and their corresponding value
    randLetters = get_rand_english_letters(language)
    # List of the random letters
    randLettersList = [i[0] for i in randLetters]
    # The random letters in a string
    randLettersString = (''.join(randLettersList)).lower()
    randPcString = computers_turn(randLettersString, language)
    # Get value of word
    wordScore = score_of_english_word(randPcString, language)
    hre = "/playerVsComputer?turn=" + turn + "&language=" + language
    return render_template('playerVsComputer.html', l=randLetters, word=randPcString, wordScore=wordScore, title='P vs Ai', hre = hre)

if __name__ == '__main__':
    app.run(debug=True)
