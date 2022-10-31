# Wordle Solver:

import math
import subprocess
import os

# Solver Client + Listener
from multiprocessing.connection import Client
from multiprocessing.connection import Listener

# TODO : Open Wordle game
#        Deocamdata deschide manual pe rand (jocul primul, dupa solver)
wordlePath = os.path.join(os.path.dirname(__file__), '..\Wordle\wordle.py')
print(wordlePath)

# Client
addressClient = ('localhost', 6000)
connClient = Client(addressClient, authkey=b'secret password')

# Listener
addressListener = ('localhost', 6001)
listener = Listener(addressListener, authkey=b'secret password')
connListener = listener.accept()
print('connection accepted from', listener.last_accepted)


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
        return

def sendBestWord(word):
    word = word.upper()
    connClient.send(word)

    # TODO : close
    # if word == "exit":
    #     connClient.close()
    #     break


listenerMsg = ''
def receiveFeedback():
    global listenerMsg

    if listenerMsg != "exit":
        listenerMsg = connListener.recv()
        print("From game : ", listenerMsg)

        # TODO : close
        # if listenerMsg == "exit":
        #     connListener.close()
        #     listener.close()

    return listenerMsg


if __name__ == '__main__':
    file = open(os.path.join(os.path.dirname(__file__), '../gameMode.txt'), 'w')
    file.write('1')
    file.close()

    words = []
    readWords(os.path.join(os.path.dirname(__file__), '../database.txt'), words)

    feedback = ""

    # Main loop
    while True:

        if feedback == "VVVVV":
            wordToSend = "exit"
        else:
            # TODO : doar pt test - trb gasit urmatorul cuvant
            wordToSend = str(input("Send to game : "))

        # Daca am gasit cuvantul corect -> termina programul
        if wordToSend == "exit":
            break

        # Altfel continua sa ghicesti
        sendBestWord(wordToSend)
        feedback = receiveFeedback()


    # while feedback != '':
    #     deleteUnwantedWords(words, feedback, bestWord)
    #
    #     bestWord = getBestWord(words)
    #     file = open(os.path.join(os.path.dirname(__file__), '../currentWord.txt'), 'w')
    #     file.write(bestWord)
    #     file.close()
    #
    #     subprocess.call(os.path.join(os.path.dirname(__file__), '../Wordle/wordle.py'), shell=True)
    #
    #     file = open(os.path.join(os.path.dirname(__file__), '../feedback.txt'), 'r')
    #     feedback = file.read()
    #     file.close()
    #
    # print(bestWord)
    #
    # file = open(os.path.join(os.path.dirname(__file__), '../gameMode.txt'), 'w')
    # file.write('0')
    # file.close()





