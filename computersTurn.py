import random


def computers_turn(letters):
    try:
        with open('./dictionary/englishWords.txt', 'r', encoding='UTF-8') as f:
            words = f.read().split()
            possibleWords = []
            for word in words:
                flag = 1
                checker = list(letters)
                for x in word:
                    if x in checker:
                        checker.remove(x)
                    else:
                        flag = 0
                        break
                if flag == 1:
                    if len(word) >= 5:
                        possibleWords.append(word) 
            rand = random.choice(possibleWords) 
            return rand
    except FileNotFoundError:
        print('file not found')