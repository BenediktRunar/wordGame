import random

def get_rand_english_letters(language):
    randLettersList = []
    if language == "english":
        lettersList = (
            'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
            'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'N', 'N', 'N', 'N',
            'N', 'N', 'R', 'R', 'R', 'R', 'R', 'R', 'T', 'T', 'T', 'T', 'T', 'T', 'L', 'L', 'L', 'L', 'S', 'S', 'S',
            'S', 'U', 'U', 'U', 'U', 'D', 'D', 'D', 'D', 'G', 'G', 'G', 'B', 'B', 'C', 'C', 'M', 'M', 'P', 'P', 'F',
            'F', 'H', 'H', 'V', 'V', 'W', 'W', 'Y', 'Y', 'K', 'J', 'X', 'Q', 'Z')
    else:
        lettersList = (
            'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 
            'S', 'S', 'S', 'S', 'S', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'T', 'T', 
            'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'U', 'U', 'L', 'L', 'L', 'L', 'L', 'K', 'K', 'K', 'K', 'Ð', 'Ð', 
            'Ð', 'Ð', 'M', 'M', 'M', 'E', 'E', 'E', 'F', 'F', 'F', 'G', 'G', 'G', 'Ó', 'Ó', 'Á', 'Á', 'Æ', 'Æ', 'Í', 
            'U', 'H', 'V', 'O', 'Ý', 'D', 'P', 'B', 'J', 'Y', 'Ö', 'É', 'Þ', 'X')
    for i in range(10):
        # Get a random letter from lettersList
        randLetter = random.choice(list(lettersList))
        # Append a tuple of (random letter, score of letter) to the random Letters List
        randLettersList.append(tuple((randLetter, score_of_english_letter(randLetter, language))))
    return randLettersList

def score_of_english_letter(letter, language):
    if language == "english":
        scores = {'A': '1', 'B': '3', 'C': '3', 'D': '2', 'E': '1', 'F': '4', 'G': '2', 'H': '4', 'I': '1', 'J': '8',
              'K': '5', 'L': '1', 'M': '3', 'N': '1', 'O': '1', 'P': '3', 'Q': '10', 'R': '1', 'S': '1', 'T': '1',
              'U': '1', 'V': '4', 'W': '4', 'X': '8', 'Y': '4', 'Z': '10'}
    else:
        scores = {'A':'1', 'R':'1', 'S':'1', 'I':'1', 'N':'1', 'T':'2', 'U':'2', 'L':'2', 'K':'2', 'Ð':'2', 'M':'2', 
            'E':'3', 'F':'3', 'G':'3', 'Ó':'3', 'Á':'3', 'Æ':'4', 'Í':'4', 'Ú':'4', 'H':'4', 'V':'5', 'O':'5', 
            'Ý':'5', 'D':'5', 'P':'5', 'B':'5', 'J':'6', 'Y':'6', 'Ö':'6', 'É':'7', 'Þ':'7', 'X':'10'}
    # dictionary with all the letters and their corresponding value
    return scores.get(letter)

def score_of_english_word(word, language):
    # Every letter in the word is evaluated in score_of_english_letter and the value is stored in a list
    # We then calculate the sum of that list and return it as a string
    return str(sum(int(score_of_english_letter(letter.upper(), language)) for letter in word))

