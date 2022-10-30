# Wordle Game

import random
import pygame
from sys import exit

SCR_WIDTH = 600
SCR_HEIGHT = 800

# PYGAME Configuration
pygame.init()
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
pygame.display.set_caption("Wordle")
pygameIcon = pygame.image.load("WordleIcon.png")
pygame.display.set_icon(pygameIcon)

clock = pygame.time.Clock()

# Background color
backgroundColor = (18, 18, 19)
screen.fill(backgroundColor)

# Text
titleFont = pygame.font.Font(None, 50)                       # TODO : ADD NEW FONT
charFont = pygame.font.Font(None, 64)                        # TODO : 64 = gridSquareSize - gridSpace * 2
textWordle = titleFont.render("Wordle", True, "White")

# Grid Configuration
squareSpace = 8             # TODO : find a good value (between squares)
gridSpace = 3               # TODO : find a good value (between grid and fill square)
gridSquareSize = 70         # TODO : find a good value (grid size)
startSquareHeight = 150     # TODO : find a good value

# Words
words = [
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0']
        ]

# N = negru
# V = verde
# G = galben
# X = neutru
feedback =  [
                ['X', 'X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X', 'X']
            ]

currentRow = 0
currentColumn = 0

endGame = False
winGame = False

# classes + functions
class Square:
    def __init__(self, gridSquareWidth, gridSquareHeight, row, column):
        self.gridSquareWidth = gridSquareWidth
        self.gridSquareHeight = gridSquareHeight
        self.row = row
        self.column = column

        self.fillSquareSize = gridSquareSize - gridSpace * 2
        self.fillSquareWidth = gridSquareWidth + gridSpace
        self.fillSquareHeight = gridSquareHeight + gridSpace

        self.gridColor = (129, 131, 132)
        self.squareColor = (18, 18, 19)
        self.blackColor = (58, 58, 60)
        self.greenColor = (83, 141, 78)
        self.yellowColor = (183, 161, 72)

    def draw(self):

        color = self.gridColor
        if feedback[self.row][self.column] == 'N':
            color = self.blackColor
        elif feedback[self.row][self.column] == 'V':
            color = self.greenColor
        elif feedback[self.row][self.column] == 'G':
            color = self.yellowColor

        pygame.draw.rect(screen, color, (self.gridSquareWidth, self.gridSquareHeight, gridSquareSize, gridSquareSize))

        if feedback[self.row][self.column] == 'X':
            pygame.draw.rect(screen, self.squareColor, (self.fillSquareWidth, self.fillSquareHeight, self.fillSquareSize, self.fillSquareSize))

        if words[self.row][self.column] != '0':
            textChar = charFont.render(words[self.row][self.column], True, "White")

            textWidth = self.fillSquareWidth + self.fillSquareSize // 2 - textChar.get_width() // 2
            textHeight = self.fillSquareHeight + self.fillSquareSize // 2 - textChar.get_height() // 2

            screen.blit(textChar, (textWidth, textHeight))

class Grid:
    def draw(self):
        for row in range(6):
            # mid square
            midSquareWidth = SCR_WIDTH // 2 - gridSquareSize // 2
            midSquareHeight = startSquareHeight + row * squareSpace + row * gridSquareSize

            for i in range(-2, 3):
                squareWidth = midSquareWidth + i * squareSpace + i * gridSquareSize
                squareHeight = midSquareHeight
                column = i + 2

                square = Square(squareWidth, squareHeight, row, column)
                square.draw()


def wordFeedback():
    global hiddenWord
    global winGame
    global endGame

    for i in range(5):
        if hiddenWord[i] == words[currentRow][i]:
            feedback[currentRow][i] = 'V'
        else:
            for j in range(5):
                if hiddenWord[j] == words[currentRow][i]:
                    feedback[currentRow][i] = 'G'
                    break
            else:
                feedback[currentRow][i] = 'N'

    if hiddenWord == "".join(words[currentRow]):
        winGame = True
        endGame = True


def checkInput(event):
    global currentRow
    global currentColumn
    global endGame

    if event.type == pygame.KEYDOWN:
        print(pygame.key.name(event.key))
        if pygame.K_a <= event.key <= pygame.K_z:
            if currentColumn < 5:
                words[currentRow][currentColumn] = pygame.key.name(event.key).upper()
                currentColumn += 1
        elif event.key == pygame.K_BACKSPACE:
            currentColumn = max(currentColumn - 1, 0)
            words[currentRow][currentColumn] = '0'
        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
            if currentColumn == 5:

                currentWord = ""
                for i in range(5):
                    currentWord += words[currentRow][i]

                if checkDataBase(currentWord):
                    print("Next word")

                    wordFeedback()

                    currentRow += 1
                    currentColumn = 0
                else:
                    print("Word isn't in database")

                if currentRow == 6:
                    endGame = True
                    print("End game")
            else:
                print("Word is not valid")  # TODO : invalid word


def checkDataBase(word):        # TODO : binary search / use a dict
    global database
    for w in database:
        if w == word:
            return True
    return False


# Database
database = []
file = open('../dataBase.txt', 'r')
fileline = file.readline()
while fileline:
    fileline = fileline[:-1]
    database.append(fileline)
    fileline = file.readline()
file.close()

# Choose a random word
hiddenWord = random.choice(database)
print("Hidden word : ", hiddenWord)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # check keyboard input
        if not endGame:
            checkInput(event)

    # draw interface
    textWidth = SCR_WIDTH // 2 - textWordle.get_width() // 2
    screen.blit(textWordle, (textWidth, 50))

    # draw grid + characters
    grid = Grid()
    grid.draw()

    # draw win/loss
    if endGame:
        strResult = "LOSER"
        colResult = "Red"
        if winGame:
            strResult = "WINNER"
            colResult = "Green"

        textResult = titleFont.render(strResult, True, colResult)
        textWidth = SCR_WIDTH // 2 - textResult.get_width() // 2
        screen.blit(textResult, (textWidth, 100))

    # refresh
    pygame.display.update()
    clock.tick(60)
    screen.fill(backgroundColor)

# TODO : Animation for each character
# TODO : Show all characters

