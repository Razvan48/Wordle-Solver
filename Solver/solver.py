# Wordle Solver:

import math
import os

# Solver Client + Listener
from multiprocessing.connection import Client
from multiprocessing.connection import Listener

#Set gameMode = 1
file = open(os.path.join(os.path.dirname(__file__), '../gameMode.txt'), 'w')
file.write('1')
file.close()

# Open Wordle game
wordlePath = os.path.join(os.path.dirname(__file__), '..\Wordle\wordle.py')
print(wordlePath)
os.startfile(wordlePath)

# Client
addressClient = ('localhost', 6000)
connClient = Client(addressClient, authkey=b'secret password')

# Listener
addressListener = ('localhost', 6001)
listener = Listener(addressListener, authkey=b'secret password')
connListener = listener.accept()
print('connection accepted from', listener.last_accepted)

ALPHABET_SIZE = 26
LETTERS_IN_WORD = 5


def getBestWord(words):

     frequency = [[0 for y in range(LETTERS_IN_WORD)] for x in range(ALPHABET_SIZE)]
     probability = [[0 for y in range(LETTERS_IN_WORD)] for x in range(ALPHABET_SIZE)]

     for word in words:
         for letterIndex in range(LETTERS_IN_WORD):
             frequency[ord(word[letterIndex]) - ord('A')][letterIndex] += 1

     for rowIndex in range(ALPHABET_SIZE):
         for columnIndex in range(LETTERS_IN_WORD):
             probability[rowIndex][columnIndex] = frequency[rowIndex][columnIndex] / len(words)

     bestWord = words[0]
     bestEntropy = 0

     for word in words:
         currentEntropy = 0
         for letterIndex in range(LETTERS_IN_WORD):
             currentEntropy += probability[ord(word[letterIndex]) - ord('A')][letterIndex] * math.log2(1 / probability[ord(word[letterIndex]) - ord('A')][letterIndex])
         if currentEntropy > bestEntropy:
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


def ok(currentWord, feedback, word):
    index = 0
    while index < len(feedback):
        if feedback[index] == 'V' and currentWord[index] != word[index]:
            return False
        elif feedback[index] == 'G' and ((not word[index] in (currentWord[:index] + currentWord[index + 1:])) or currentWord[index] == word[index]):
            return False
        elif feedback[index] == 'N' and (word[index] in currentWord):
            return False
        index += 1

    return True


def deleteUnwantedWords(words, feedback, word):
    if feedback == "":
        return

    words.remove(word)

    index = 0
    while index < len(words):
        if not ok(words[index], feedback, word):
            words.remove(words[index])
            index -= 1
        index += 1


def sendBestWord(word):
    word = word.upper()
    connClient.send(word)
    print("Send to game : ", word)


listenerMsg = ''
def receiveFeedback():
    global listenerMsg

    if listenerMsg != "exit":
        listenerMsg = connListener.recv()
        print("From game : ", listenerMsg)

    return listenerMsg


def closeConnection():
    connClient.close()
    connListener.close()
    listener.close()
    

words = []
readWords(os.path.join(os.path.dirname(__file__), '../database.txt'), words)

feedback = ""
file = open(os.path.join(os.path.dirname(__file__), '../gameMode.txt'), 'w')
file.write('0')
file.close()

# Main loop
while True:

    if feedback == "VVVVV":
        wordToSend = "exit"
    else:
        wordToSend = getBestWord(words)

    # Daca am gasit cuvantul corect -> termina programul
    if wordToSend == "exit":
        break

    # Altfel continua sa ghicesti
    sendBestWord(wordToSend)
    feedback = receiveFeedback()

    deleteUnwantedWords(words, feedback, wordToSend)

closeConnection()

