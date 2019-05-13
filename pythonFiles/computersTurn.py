import random
def computersTurn(letters):
    print(letters)
    words = []
    possibleWords = []
    try:
        with open('./dictionary/englishWords.txt', 'r', encoding='UTF-8') as f:
            words = f.read().split()
            for word in words:
                flag = 1
                checker = list(letters)
                for i in range(len(word)):
                    if word[i] in checker:
                        checker.remove(word[i])
                    else:
                        flag = 0
                        break
                if flag == 1:
                    possibleWords.append(word)    
        rand = random.choice(possibleWords)                
    except FileNotFoundError:
        print('file not found')
    return rand

print(computersTurn('tiantmuogsselom'))
