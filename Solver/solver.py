# Test Solver:

import math

def getBestWord(words):

    ALPHABET_SIZE = 26
    LETTERS_IN_WORD = 5

    frequency = [[0 for y in range(LETTERS_IN_WORD)] for x in range(ALPHABET_SIZE)]
    probability = [[0 for y in range(LETTERS_IN_WORD)] for x in range(ALPHABET_SIZE)]

    for word in words:
        for letterIndex in range(LETTERS_IN_WORD):
            frequency[ord(word[letterIndex]) - ord('A')][letterIndex] += 1

    for rowIndex in range(ALPHABET_SIZE):
        for columnIndex in range(LETTERS_IN_WORD):
            probability[rowIndex][columnIndex] = frequency[rowIndex][columnIndex] / len(words)

    bestWord = words[0]
    bestEntropy = math.inf

    for word in words:
        currentEntropy = 0
        for letterIndex in range(LETTERS_IN_WORD):
            currentEntropy += frequency[ord(word[letterIndex]) - ord('A')][letterIndex] * math.log2(1 / probability[ord(word[letterIndex]) - ord('A')][letterIndex])
        if currentEntropy < bestEntropy:
            bestEntropy = currentEntropy
            bestWord = word

    return bestWord


def readWords(address, words):
    words.clear()
    file = open(address, 'r')
    fileline = file.readline()
    while fileline:
        words.append(fileline)
        fileline = file.readline()
    file.close()

    index = 0
    while index < len(words):
        words[index] = words[index][:-1]
        index += 1


def deleteUnwantedWords(words, feedback, word):              #TO DO
    if feedback == '':
        return;

    # TO DO


if __name__ == '__main__':
    file = open('../gameMode.txt', 'w')
    file.write('1')
    file.close()

    words = []
    readWords('../dataBase.txt', words)

    feedback = ''

    while feedback != '':
        deleteUnwantedWords(words, feedback, bestWord)

        bestWord = getBestWord(words)
        file = open('../currentWord.txt', 'w')
        file.write(bestWord)
        file.close()

        exec('../Wordle/wordle.py')

        file = open('../feedback.txt', 'r')
        feedback = file.read()
        file.close()

    print(bestWord)

    file = open('../gameMode.txt', 'w')
    file.write('0')
    file.close()





