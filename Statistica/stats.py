import os

# importa metodele de rezolvare din sol.py
from sol import solution1
from sol import solution2

sol = solution1()       # TODO : solution1 / solution2
def getFeedback(word, hiddenWord):
    feedback = []
    for i in range(5):
        if hiddenWord[i] == word[i]:
            feedback.append('V')
        else:
            for j in range(5):
                if hiddenWord[j] == word[i]:
                    feedback.append('G')
                    break
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
    file = open(os.path.join(os.path.dirname(__file__), "metoda1Cuvinte.txt"), 'w')
    suma = 0
    outputInFile = ""
    for i in range(len(database)):
        hiddenWord = database[i]
        endGame = False
        words = database.copy()
        lant_incercari = []
        while True:
            bestWord = sol.getBestWord(words)
            lant_incercari.append(bestWord)
            feedback = getFeedback(bestWord, hiddenWord)
            sol.deleteUnwantedWords(words, feedback, bestWord)
            if bestWord == hiddenWord:
                endGame = True
            # Next Word
            if endGame:
                suma += len(lant_incercari)
                outputInFile += "CUVANT: " + hiddenWord + "\n" + "NUMAR INCERCARI: " + str(len(lant_incercari)) + "\n"
                # file.write("CUVANT: " + hiddenWord)
                # file.write("\n")
                # file.write("NUMAR INCERCARI: " + str(len(lant_incercari)))
                # file.write("\n")

                for i in range(len(lant_incercari)):
                    #file.write(lant_incercari[i] + " ")
                    outputInFile += str(lant_incercari[i]) + " "
                #file.write("\n\n")
                outputInFile += "\n\n"
                break
                #print(hiddenWord)

    file.close()
    file = open(os.path.join(os.path.dirname(__file__), "medie1.txt"), 'w')
    medie = suma / len(database)
    file.write("Media este: " + str(medie))
    file.close()
    # Scrie in medie.txt media finala

# TODO : statistica pt ambele solutii in 2 fisiere diferite

