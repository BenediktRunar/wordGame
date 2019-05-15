from scoreOfLetters import *
class Square:
    def __init__(self, letter):
        self.letter = letter
        self.value = scoreOfLetter(letter)




# def playerVsComputer():
#     language = request.args.get('language')
#     turn = request.args.get('turn')
#     if turn == '1':
#         turn = '2'
#         hre = "/playerVsComputer?turn=" + turn + "&language=" + language
#         # List of tuples with random letters and their corresponding value
#         randLetters = get_rand_english_letters(language)
#         return render_template('playerVsComputer.html', l=randLetters, title='P vs Ai', hre = hre)
#     else:
#         turn = '1'
#         # List of tuples with random letters and their corresponding value
#         randLetters = get_rand_english_letters(language)
#         # List of the random letters
#         randLettersList = [i[0] for i in randLetters]
#         # The random letters in a string
#         randLettersString = (''.join(randLettersList)).lower()
#         randPcString = computers_turn(randLettersString, language)
#         # Get value of word
#         wordScore = score_of_english_word(randPcString, language)
#         hre = "/playerVsComputer?turn=" + turn + "&language=" + language
        
#     return render_template('playerVsComputer.html', l=randLetters, word=randPcString, wordScore=wordScore, title='P vs Ai', hre = hre)
