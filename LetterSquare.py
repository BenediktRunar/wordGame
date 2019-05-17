from scoreOfLetters import *
class Square:
    def __init__(self, letter):
        self.letter = letter
        self.value = scoreOfLetter(letter)
