# Wordle Game

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
testFont = pygame.font.Font(None, 50)                       # TODO : ADD NEW FONT
textWordle = testFont.render("Wordle", True, "White")       # TODO : TRUE/FALSE


class Square:
    def __init__(self, gridSquareWidth, gridSquareHeight, gridSquareSize, gridSpace):
        self.gridSquareWidth = gridSquareWidth
        self.gridSquareHeight = gridSquareHeight
        self.gridSquareSize = gridSquareSize
        self.gridSpace = gridSpace

        self.fillSquareSize = gridSquareSize - gridSpace * 2
        self.fillSquareWidth = gridSquareWidth + gridSpace
        self.fillSquareHeight = gridSquareHeight + gridSpace

        self.gridColor = (129, 131, 132)
        self.squareColor = (18, 18, 19)

        global screen

    def draw(self):
        pygame.draw.rect(screen, self.gridColor, (self.gridSquareWidth, self.gridSquareHeight, self.gridSquareSize, self.gridSquareSize))
        pygame.draw.rect(screen, self.squareColor, (self.fillSquareWidth, self.fillSquareHeight, self.fillSquareSize, self.fillSquareSize))


class Grid:
    def __init__(self, squareSpace = 8, gridSpace = 3, gridSquareSize = 70, startSquareHeight = 200):
        self.squareSpace = squareSpace                  # TODO : find a good value (between squares)
        self.gridSpace = gridSpace                      # TODO : find a good value (between grid and fill square)
        self.gridSquareSize = gridSquareSize            # TODO : find a good value (grid size)
        self.startSquareHeight = startSquareHeight      # TODO : find a good value

        global SCR_WIDTH

    def draw(self):
        for k in range(6):
            # mid square
            midSquareWidth = SCR_WIDTH // 2 - self.gridSquareSize // 2
            midSquareHeight = self.startSquareHeight + k * self.squareSpace + k * self.gridSquareSize
            midSquare = Square(midSquareWidth, midSquareHeight, self.gridSquareSize, self.gridSpace)
            midSquare.draw()

            # left squares 1/2
            for i in range(1, 3):
                leftSquareWidth = midSquare.gridSquareWidth - i * self.squareSpace - i * self.gridSquareSize
                leftSquareHeight = midSquare.gridSquareHeight
                leftSquare = Square(leftSquareWidth, leftSquareHeight, self.gridSquareSize, self.gridSpace)
                leftSquare.draw()

            # right squares 1/2
            for i in range(1, 3):
                rightSquareWidth = midSquare.gridSquareWidth + i * self.squareSpace + i * self.gridSquareSize
                rightSquareHeight = midSquare.gridSquareHeight
                rightSquare = Square(rightSquareWidth, rightSquareHeight, self.gridSquareSize, self.gridSpace)
                rightSquare.draw()


# Game
currentWord = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # check keyboard input
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            if pygame.K_a <= event.key <= pygame.K_z:
                if len(currentWord) < 5:
                    currentWord += pygame.key.name(event.key)
            elif event.key == pygame.K_BACKSPACE:
                currentWord = currentWord[:-1]
            elif event.key == pygame.K_RETURN:
                pass        # TODO : next word

    # draw interface
    textWidth = SCR_WIDTH // 2 - textWordle.get_width() // 2
    screen.blit(textWordle, (textWidth, 50))

    # draw grid
    grid = Grid()
    grid.draw()

    # draw current word
    textCurrentWord = testFont.render(currentWord, True, "White")
    textWidth = SCR_WIDTH // 2 - textCurrentWord.get_width() // 2
    screen.blit(textCurrentWord, (200, 200))

    # refresh
    pygame.display.update()
    clock.tick(60)
    screen.fill(backgroundColor)

# TODO : Animation for each character
# TODO : Change grind color to white if there is a character there

