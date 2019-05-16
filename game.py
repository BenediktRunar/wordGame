from letters import *
from computersTurn import *

def PlayerTurn(userWord, language, randLettersString, turn, game):
    score = 0
        # Check if former word is valid
    score = 0
    if userWord and userWord != 'invalidUserWord':
        userWord = userWord.lower()
        if check_if_valid(userWord, language):
            score = score_of_word(userWord, language)
        else:
            return  game + "?language=" + language + "&randLettersString=" + randLettersString + '&userWord=invalidUserWord'
    # If the word-before is correct
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

    url = getUrl(game, turn, language, randLettersString)

    return url, randLetters, score


def getUrl(game, turn, language, randLettersString):
    url = game + "?language=" + language + "&randLettersString=" + randLettersString
    
    if game == "/twoPlayer":
        print("halllllo")
        if turn == '1':
            turn = '2'  
        else:
            turn = '1'
        url += '&turn=' + turn
    return url