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
    userWord = request.args.get('userWord')
    language = request.args.get('language')
    randLettersString = request.args.get('randLettersString')

    if userWord and userWord != 'invalidUserWord':
        userWord = userWord.lower()
        print(userWord)
        if check_if_valid(userWord, language):
            score = score_of_english_word(userWord, language)
            print(score)
        else:
            return redirect("/playerVsComputer?language=" + language + "&randLettersString=" + randLettersString + '&userWord=invalidUserWord')
    
    if userWord != 'invalidUserWord':
        # List of tuples with random letters and their corresponding value
        randLetters = get_rand_english_letters(language)
        # List of the random letters
        randLettersList = [i[0] for i in randLetters]
        randLettersString = (''.join(randLettersList)).lower()
    else:
        randLetters = string_to_tuple(randLettersString, language)

    hre = "/playerVsComputer?language=" + language + "&randLettersString=" + randLettersString + '&userWord='

    
    ##Computers turn
    # List of tuples with random letters and their corresponding value
    randLettersForComputer = get_rand_english_letters(language)
    # List of the random letters
    randLettersListForComputer = [i[0] for i in randLettersForComputer]
    # The random letters in a string
    randLettersString = (''.join(randLettersListForComputer)).lower()
    randPcString = computers_turn(randLettersString, language)
    # Get value of word
    wordScore = score_of_english_word(randPcString, language)
    # print("letters: ", randLettersListForComputer, " word: ", randPcString, " score: ", wordScore)
    return render_template('playerVsComputer.html', l=randLetters, title='P vs Ai', hre = hre)

if __name__ == '__main__':
    app.run(debug=True)
