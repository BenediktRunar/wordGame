from flask import Flask, render_template, url_for, request, redirect
from letters import *
from computersTurn import *

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

def testtt(userWord, language, randLettersString, turn, game):
        # Check if former word is valid
    if userWord and userWord != 'invalidUserWord':
        userWord = userWord.lower()
        if check_if_valid(userWord, language):
            score = score_of_word(userWord, language)
        else:
            return  game + "?language=" + language + "&randLettersString=" + randLettersString + '&userWord=invalidUserWord'
    # If the word before is correct
    if userWord != 'invalidUserWord':
        # List of tuples with random letters and their corresponding value
        randLetters = get_rand_letters(language)
        # List of the random letters
        randLettersList = [i[0] for i in randLetters]
        # random letters from tuple to string
        randLettersString = (''.join(randLettersList)).lower()
        # If there is a word to check on

        if game == "/playerVsComputer" and userWord != None:
            compWor = computers_turn(language)
    else:
        # Getting the last letters, making them into tuple
        randLetters = string_to_tuple(randLettersString, language)

    hre = game + "?language=" + language + "&randLettersString=" + randLettersString + '&userWord='
    if game == "/twoPlayer":
        print("halllllo")
        if turn == '1':
            turn = '2'  
        else:
            turn = '1'
        hre = game + "?language=" + language + "&randLettersString=" + randLettersString + '&turn=' + turn + '&userWord='
    return hre, randLetters

# Game: Two player
@app.route("/twoPlayer")
def TwoPlayer():
    # Getting information from url
    userWord = request.args.get('userWord')
    language = request.args.get('language')
    randLettersString = request.args.get('randLettersString')
    turn = request.args.get('turn')
    game = "/twoPlayer"

    testst = testtt(userWord, language, randLettersString, turn, game)

    if type(testst) == str:
        return redirect(testst) 
    else:
        # print("letters: ", randLettersListForComputer, " word: ", randPcString, " score: ", wordScore)
        return render_template('playerVsComputer.html', l=testst[1], title='P vs Ai', hre = testst[0])

@app.route("/playerVsComputer")
def playerVsComputer():
    # Getting information from url
    userWord = request.args.get('userWord')
    language = request.args.get('language')
    randLettersString = request.args.get('randLettersString')
    game = "/playerVsComputer"

    testst = testtt(userWord, language, randLettersString, 0, game)

    if type(testst) == str:
        return redirect(testst) 
    else:
        # print("letters: ", randLettersListForComputer, " word: ", randPcString, " score: ", wordScore)
        return render_template('playerVsComputer.html', l=testst[1], title='P vs Ai', hre = testst[0])

if __name__ == '__main__':
    app.run(debug=True)