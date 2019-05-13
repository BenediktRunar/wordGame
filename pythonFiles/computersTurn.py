import random
def computersTurn(letters):
    try:
        with open('./dictionary/englishWords.txt', 'r', encoding='UTF-8') as f:
            words = f.read().split()
            possibleWords = []
            for i in range(len(words)):
                flag = 1
                checker = list(letters)
                for x in range(len(words[i])):
                    if words[i][x] in checker:
                        checker.remove(words[i][x])
                    else:
                        flag = 0
                        break
                if flag == 1:
                    possibleWords.append(words[i]) 
            rand = random.choice(possibleWords) 
            return rand
    except FileNotFoundError:
        print('file not found')

