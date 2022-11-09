import os

# importa metodele de rezolvare din sol.py
from sol import solution1
from sol import solution2

def getFeedback(word):
    # N = negru
    # V = verde
    # G = galben
    # X = neutru
    # pt word genereaza feedback -> 
    return "VVVVV"      # TODO 


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

        # Lista cuvinte posibile (o modificam in functie de feedback)
        words = database

        while True:
            # genereaza urmatorul cuvant folosind functia din solver -> getBestWorld
            bestWord = solution1.getBestWord(words)

            # verifica cuvantul si trimite feedback
            feedback = getFeedback(bestWord)

            # actualizeaza lista
            solution1.deleteUnwantedWords(words, feedback, bestWord)

            # Next Word
            if endGame:
                # Scrie in medie.txt rezultatul:
                # "CUVANT" - "NR INCERCARI"

                break

    
    # Scrie in medie.txt media finala

# TODO : statistica pt ambele solutii in 2 fisiere diferite

