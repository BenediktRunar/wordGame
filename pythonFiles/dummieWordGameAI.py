import random

def computer_words(letters):
    # The chars that the word must consist of are in #letter

    # The list of words that can be created with those chars
    possibleWords = []

    with open(filename, 'r') as dictionary:
        for word in dictionary:
    return None


def countdown(filename, inputString):



    with open(filename, 'r') as dictionary:
        for word in dictionary:
            # whitespace cleared
            word = word.strip()

            # if the word is longer than or equal to 4 AND
            # if the word is shorter than or equal to the length of the inputString (should be 9)
            if (len(word) >= 4 and len(word) <= len(inputString)):
                if (any(char in word for char in set(inputCharsList))):
                    # if every char of the word is in the inputCharsList as often as it is in the word or less
                    if (all(word.count(char) <= inputCharsList.count(char) for char in set(word))):
                        # The word is added to the list of possibleWords
                        possibleWords.append(word)

    return sorted(possibleWords)