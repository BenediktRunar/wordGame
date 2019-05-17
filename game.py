from letters import *
from computersTurn import *

def PlayerTurn(userWord, language, turn, game, randLettersString):
    # Check if former word is valid
    print("turn",turn)
    url = game
    score = 0
    #EF það er búið að setja inn eitthvað orð
    if userWord :
        #Gáum hvort það sé rétt
        if check_if_valid(userWord.lower(), language):
            score = score_of_word(userWord, language)
            #url = getUrl(url, turn) 
            print(userWord, 'is valid', url)

            #Ef það verið að spila við tölvu gerir hún hér
            if game == "/playerVsComputer" and userWord != None:
                compWor = computers_turn(language)
            #Þurfum nýja
        else:
            userWord = 'invalidUserWord'
            print('invalid')
            # Getting the last letters, making them into tuple
            randLetters = string_to_tuple(randLettersString, language)
            url += '?turn=' + turn
            return url, randLetters, score, userWord
    
        
    ####### Það er ekkert orð eða orðið er rétt svo við initializum
    # List of tuples with random letters and their corresponding value
    randLetters = get_rand_letters(language)
    # List of the random letters
    randLettersList = [i[0] for i in randLetters]
    # random letters from tuple to string
    randLettersString = (''.join(randLettersList)).lower()

    url = getUrl(url, turn) 

    return url, randLetters, score, userWord


def getUrl(url, turn):
    if url == "/twoPlayer":
        if turn == '1':
            turn = '2'  
        else:
            turn = '1'
        url += '?turn=' + turn
    return url