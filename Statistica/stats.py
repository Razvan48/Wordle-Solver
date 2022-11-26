import os

#Importa metoda de rezolvare din sol.py
from sol import solution
sol = solution()

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


# Database
database = []
file = open(os.path.join(os.path.dirname(__file__), "../database.txt"), 'r')
fileline = file.readline()
while fileline:
    fileline = fileline[:-1]
    database.append(fileline)
    fileline = file.readline()
file.close()

tries_output = ""
total_tries = 0
for i in range(len(database)):
    hiddenWord = database[i]
    endGame = False
    words = database.copy()
    tries_output += hiddenWord + ": "
    number_of_tries = 0
    while True:
        bestWord = sol.getBestWord(words)
        feedback = getFeedback(bestWord, hiddenWord)
        sol.deleteUnwantedWords(words, feedback, bestWord)

        number_of_tries += 1
        if bestWord == hiddenWord:
            total_tries += number_of_tries
            tries_output += bestWord + " "
            tries_output += "\n"
            break
        else:
            tries_output += bestWord + ", "
file = open(os.path.join(os.path.dirname(__file__), "solutii.txt"), 'w')
file.write(tries_output)
file.close()

average = total_tries / len(database)
file = open(os.path.join(os.path.dirname(__file__), "medie.txt"), 'w')
file.write("Media este: " + str(average))
file.close()