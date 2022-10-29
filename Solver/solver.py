# Test Solver:

def getBestWord(words):

    ALPHABET_SIZE = 26
    LETTERS_IN_WORD = 5

    frequency = [[0 for y in range(LETTERS_IN_WORD)] for x in range(ALPHABET_SIZE)]

    for word in words:
        for letterIndex in range(LETTERS_IN_WORD):
            frequency[ord(word[letterIndex]) - ord('A')][letterIndex] += 1

    for rowIndex in range(ALPHABET_SIZE):
        for columnIndex in range(LETTERS_IN_WORD):
            frequency[rowIndex][columnIndex] /= len(words)

    bestWord = words[0]
    bestInformation = 0

    for word in words:
        currentInformation = 0
        for letterIndex in range(LETTERS_IN_WORD):
            currentInformation += frequency[ord(word[letterIndex]) - ord('A')][letterIndex]
        if currentInformation > bestInformation:
            bestInformation = currentInformation
            bestWord = word

    #Pentru debug
    #for rowIndex in range(ALPHABET_SIZE):
    #    for columnIndex in range(LETTERS_IN_WORD):
    #        print(frequency[rowIndex][columnIndex], end=' ')
    #    print('\n')

    return bestWord


def readWords(address, words):
    words.clear()
    file = open(address, "r")
    fileline = file.readline()
    while fileline:
        words.append(fileline)
        fileline = file.readline()
    index = 0
    while index < len(words):
        words[index] = words[index][:-1]
        index += 1


if __name__ == '__main__':
    words = []
    readWords('../database.txt', words)
    print(getBestWord(words))




