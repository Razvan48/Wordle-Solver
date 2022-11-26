import os

# importa metodele de rezolvare din sol.py
from sol import solution1
from sol import solution2
from sol import solution3

#sol = solution1() # TODO : solution1 / solution2
sol = solution2()
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

    tries_output = " "
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
            tries_output += bestWord + " "
            number_of_tries += 1
            if bestWord == hiddenWord:
                number_of_tries -= 1
                total_tries += number_of_tries
                tries_output += "\n"
                break
                #print(hiddenWord)
    #file = open(os.path.join(os.path.dirname(__file__), "metoda1Cuvinte.txt"), 'w')
    file = open(os.path.join(os.path.dirname(__file__), "metoda2Cuvinte.txt"), 'w')
    file.write(tries_output)
    file.close()
    #file = open(os.path.join(os.path.dirname(__file__), "medie1.txt"), 'w')
    file = open(os.path.join(os.path.dirname(__file__), "medie2.txt"), 'w')
    average = total_tries / len(database)
    file.write("Media este: " + str(average))
    file.close()

