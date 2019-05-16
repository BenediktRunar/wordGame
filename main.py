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
@app.route("/twoPlayer")
def TwoPlayer():
    # Getting information from url
    userWord = request.args.get('userWord')
    language = request.args.get('language')
    randLettersString = request.args.get('randLettersString')
    turn = request.args.get('turn')
    game = "/twoPlayer"

    infoFromTurn = PlayerTurn(userWord, language, randLettersString, turn, game)

    if type(infoFromTurn) == str:
        return redirect(infoFromTurn) 
    else:
        # print("letters: ", randLettersListForComputer, " word: ", randPcString, " score: ", wordScore)
        return render_template('playerVsComputer.html', l=infoFromTurn[1], title='P vs Ai', hre = infoFromTurn[0], score = infoFromTurn[3])

@app.route("/playerVsComputer")
def playerVsComputer():
    # Getting information from url
    userWord = request.args.get('userWord')
    language = request.args.get('language')
    randLettersString = request.args.get('randLettersString')
    game = "/playerVsComputer"

    infoFromTurn = PlayerTurn(userWord, language, randLettersString, '0', game)

    if type(infoFromTurn) == str:
        return redirect(infoFromTurn) 
    else:
        # print("letters: ", randLettersListForComputer, " word: ", randPcString, " score: ", wordScore)
        return render_template('playerVsComputer.html', l=infoFromTurn[1], title='P vs Ai', hre = infoFromTurn[0], score = infoFromTurn[3])

if __name__ == '__main__':
    app.run(debug=True)