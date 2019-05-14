import random
def letters():
    letters = (
        'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
        'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'N', 'N', 'N', 'N', 
        'N', 'N', 'R', 'R', 'R', 'R', 'R', 'R', 'T', 'T', 'T', 'T', 'T', 'T', 'L', 'L', 'L', 'L', 'S', 'S', 'S', 
        'S', 'U', 'U', 'U', 'U', 'D', 'D', 'D', 'D', 'G', 'G', 'G', 'B', 'B', 'C', 'C', 'M', 'M', 'P', 'P', 'F', 
        'F', 'H', 'H', 'V', 'V', 'W', 'W', 'Y', 'Y', 'K', 'J', 'X', 'Q', 'Z')
    rand = []
    for i in range(15):
        thisval = random.choice(list(letters))
        rand.append(tuple((thisval, scoreOfLetter(thisval))))
    return rand

def scoreOfLetter(letter):
    scores = {'A': '1', 'B': '3', 'C': '3', 'D': '2', 'E': '1', 'F': '4', 'G': '2', 'H': '4', 'I': '1', 'J': '8', 'K': '5', 'L': '1', 'M': '3', 'N': '1', 'O': '1', 'P': '3', 'Q': '10', 'R': '1', 'S': '1', 'T': '1', 'U': '1', 'V': '4', 'W': '4', 'X': '8', 'Y': '4', 'Z': '10'}
    return scores.get(letter)