import random


def get_rand_letters():
    randLettersList = []

    lettersList = (
        'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
        'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'N', 'N', 'N', 'N',
        'N', 'N', 'R', 'R', 'R', 'R', 'R', 'R', 'T', 'T', 'T', 'T', 'T', 'T', 'L', 'L', 'L', 'L', 'S', 'S', 'S',
        'S', 'U', 'U', 'U', 'U', 'D', 'D', 'D', 'D', 'G', 'G', 'G', 'B', 'B', 'C', 'C', 'M', 'M', 'P', 'P', 'F',
        'F', 'H', 'H', 'V', 'V', 'W', 'W', 'Y', 'Y', 'K', 'J', 'X', 'Q', 'Z')

    for i in range(10):
        # Get a random letter from lettersList
        randLetter = random.choice(list(lettersList))

        # Append a tuple of (random letter, score of letter) to the random Letters List
        randLettersList.append(tuple((randLetter, score_of_letter(randLetter))))
    return randLettersList


def score_of_letter(letter):
    # dictionary with all the letters and their corresponding value
    scores = {'A': '1', 'B': '3', 'C': '3', 'D': '2', 'E': '1', 'F': '4', 'G': '2', 'H': '4', 'I': '1', 'J': '8',
              'K': '5', 'L': '1', 'M': '3', 'N': '1', 'O': '1', 'P': '3', 'Q': '10', 'R': '1', 'S': '1', 'T': '1',
              'U': '1', 'V': '4', 'W': '4', 'X': '8', 'Y': '4', 'Z': '10'}
    return scores.get(letter)


def score_of_word(word):
    # Every letter in the word is evaluated in score_of_letter and the value is stored in a list
    # We then calculate the sum of that list and return it
    return sum([score_of_letter(letter) for letter in word])
