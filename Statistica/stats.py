import os

# importa metodele de rezolvare din sol.py
from sol import solution1
from sol import solution2

sol = solution1()       # TODO : solution1 / solution2
def getFeedback(word, hiddenWord):
    nr_letters = 5
    feedback = []
    for i in range(nr_letters):
        if hiddenWord[i] == word[i]:
            feedback.append('V')
        elif word[i] in hiddenWord:
            feedback.append('G')
        else:
            feedback.append('N')
    return feedback

if __name__ == '__main__':

    # Database
    database = []
    file = open(os.path.join(os.path.dirname(__file__), "../database.txt"), 'r')
    fileline = file.readline()
    while fileline:
        fileline = fileline[:-1]
        database.append(fileline)
        fileline = file.readline()
    file.close()
    for i in range(len(database)):
        hiddenWord = database[i]
        endGame = False
        number_of_tries = 0
        # Lista cuvinte posibile (o modificam in functie de feedback)
        words = database
        #file = open(os.path.join(os.path.dirname(__file__), "medie1.txt"), 'a')
        #file.write("x")
        while endGame == False:
            bestWord = sol.getBestWord(words)
            number_of_tries += 1
            feedback = getFeedback(bestWord, hiddenWord)
            sol.deleteUnwantedWords(words, feedback, bestWord)
            if bestWord == hiddenWord:
                endGame = True
            # Next Word
            if endGame:
                #file = open(os.path.join(os.path.dirname(__file__), "medie1.txt"), 'w')
                #file.write("NR INCERCARI: " + number_of_tries)
                #file.write("\n")
                #file.close()
                print(hiddenWord)


    # Scrie in medie.txt media finala

# TODO : statistica pt ambele solutii in 2 fisiere diferite

