from letters import *
from computersTurn import *

def PlayerTurn(userWord, language, turn, game, randLettersString):
    url = game
    ####### Það er ekkert orð eða orðið er rétt svo við initializum
    # List of tuples with random letters and their corresponding value
    randLetters = get_rand_letters(language)
    #url = getUrl(url, turn) 
    return url, randLetters


def getUrl(url, turn):
    if url == "/twoPlayer":
        if turn == '1':
            turn = '2'  
        else:
            turn = '1'
        url += '?turn=' + turn
    return url


def ValidateWord(userWord, language, randLettersString):
    #EF það er búið að setja inn eitthvað orð
    if userWord and not check_if_valid(userWord.lower(), language):
        userWord = ''
    return userWord