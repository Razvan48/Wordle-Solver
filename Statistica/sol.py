import math

ALPHABET_SIZE = 26
LETTERS_IN_WORD = 5


# class solution:
#     def getBestWord(self, words):
#
#         frequency = [[0 for y in range(LETTERS_IN_WORD)] for x in range(ALPHABET_SIZE)]
#         probability = [[0 for y in range(LETTERS_IN_WORD)] for x in range(ALPHABET_SIZE)]
#
#         for word in words:
#             for letterIndex in range(LETTERS_IN_WORD):
#                 frequency[ord(word[letterIndex]) - ord('A')][letterIndex] += 1
#
#         for rowIndex in range(ALPHABET_SIZE):
#             for columnIndex in range(LETTERS_IN_WORD):
#                 probability[rowIndex][columnIndex] = frequency[rowIndex][columnIndex] / len(words)
#
#         bestWord = words[0]
#         bestInformation = 0
#
#         for word in words:
#             currentInformation = 0
#             for letterIndex in range(LETTERS_IN_WORD):
#                 currentInformation += frequency[ord(word[letterIndex]) - ord('A')][letterIndex]
#             if currentInformation > bestInformation:
#                 bestInformation = currentInformation
#                 bestWord = word
#
#         return bestWord
#
#     def ok(self, currentWord, feedback, word):
#         index = 0
#         while index < len(feedback):
#             if feedback[index] == 'V' and currentWord[index] != word[index]:
#                 return False
#             elif feedback[index] == 'G' and ((not word[index] in (currentWord[:index] + currentWord[index + 1:])) or currentWord[index] == word[index]):
#                 return False
#             elif feedback[index] == 'N' and (word[index] in currentWord):
#                 return False
#             index += 1
#
#         return True
#
#     def deleteUnwantedWords(self, words, feedback, word):
#         if feedback == "":
#             return
#
#         words.remove(word)
#
#         index = 0
#         while index < len(words):
#             if not self.ok(words[index], feedback, word):
#                 words.remove(words[index])
#                 index -= 1
#             index += 1


class solution:
    def getBestWord(self, words):
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
                currentEntropy += frequency[ord(word[letterIndex]) - ord('A')][letterIndex] * math.log2(1 / probability[ord(word[letterIndex]) - ord('A')][letterIndex])
            if currentEntropy > bestEntropy:
                bestEntropy = currentEntropy
                bestWord = word

        return bestWord


    def ok(self, currentWord, feedback, word):
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


    def deleteUnwantedWords(self, words, feedback, word):
        if feedback == "":
            return

        words.remove(word)
        
        index = 0
        while index < len(words):
            if not self.ok(words[index], feedback, word):
                words.remove(words[index])
                index -= 1
            index += 1

