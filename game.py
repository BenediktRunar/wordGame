from letters import *
from computersTurn import *

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