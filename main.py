from flask import Flask, render_template, url_for, request, redirect
from letters import *
from computersTurn import *
from game import *

app = Flask(__name__)

# home site
@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', title='Home')

# Routing site to go to correct game mode
@app.route("/routingToGame")
def routingToGame():
    # Getting information from url
    language= request.args.get('language')
    game = request.args.get('game')
    # Making correct url to go to
    if game == "twoPlayer":
        temp = "/twoPlayer?language=" + language + "&turn=1"
    else:
        temp = "/playerVsComputer?language=" + language
    # Redirect to correct site, making turn = 1 so you start your turn
    return redirect(temp) 

# Game: Two player
@app.route("/twoPlayer", methods = ['GET','POST'])
def TwoPlayer():
    if request.method == 'POST':
        userWord = request.form['userWord']
        language = request.form['language']
        randLettersString = request.form['randLettersString']
    else:
        # Getting information from url
        userWord = request.args.get('userWord')
        language = request.args.get('language')
        randLettersString = request.args.get('randLettersString')
    turn = request.args.get('turn')
    game = "/twoPlayer"

    infoFromTurn = PlayerTurn(userWord, language, turn, game, randLettersString)

    if infoFromTurn[3] == 'invalidUserWord':
        lettertuples = string_to_tuple(randLettersString, language)
    else:
        # List of the random letters
        randLettersList = [i[0] for i in infoFromTurn[1]]
        # random letters from tuple to string
        randLettersString = (''.join(randLettersList)).lower()
        # print("letters: ", randLettersListForComputer, " word: ", randPcString, " score: ", wordScore)
        lettertuples = infoFromTurn[1]
    return render_template('playerVsComputer.html', l=lettertuples, url=infoFromTurn[0], score = infoFromTurn[2], language = language, randLettersString = randLettersString)

@app.route("/playerVsComputer", methods = ['GET','POST'])
def playerVsComputer():
    # Getting information from url
    if request.method == 'POST':
        userWord = request.form['userWord']
        language = request.form['language']
        randLettersString = request.form['randLettersString']
    else:
        userWord = None
        language = request.args.get('language')
        randLettersString = request.args.get('randLetterString')
    game = "/playerVsComputer"

    infoFromTurn = PlayerTurn(userWord, language, '0', game, randLettersString)
  
    if infoFromTurn[3] == 'invalidUserWord':
        lettertuples = string_to_tuple(randLettersString, language)
    else:
        # List of the random letters
        randLettersList = [i[0] for i in infoFromTurn[1]]
        # random letters from tuple to string
        randLettersString = (''.join(randLettersList)).lower()
        # print("letters: ", randLettersListForComputer, " word: ", randPcString, " score: ", wordScore)
        lettertuples = infoFromTurn[1]
    return render_template('playerVsComputer.html', l=lettertuples, url = infoFromTurn[0], score = infoFromTurn[2], language = language, randLettersString = randLettersString)

if __name__ == '__main__':
    app.run(debug=True)