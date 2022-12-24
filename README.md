# Wordle Solver 
The first project in the course [Computer Systems Architecture](https://cs.unibuc.ro/~crusu/asc/index.html)

<p>
  <img align = "left" width="400" height="533" src="https://github.com/Razvan48/Wordle-Solver/blob/main/gifs/player%20input.gif">
  <img align = "right" width="400" height="533" src="https://github.com/Razvan48/Wordle-Solver/blob/main/gifs/solver%20input.gif">
</p>

<br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/>

## Team Members:

    1. Căpățînă Răzvan Nicolae      - 152
    2. Mihalache Sebastian Ștefan   - 152 ([https://github.com/sebimih13](https://github.com/sebimih13))
    3. Petre-Șoldan Adela           - 131 ([https://github.com/adelp13](https://github.com/adelp13))

Average number of attempts to guess the words  &rarr;  __4.91871835166754__  
The chain of attempts for each word (in the database) is written in the file [__solutii.txt__](https://github.com/Razvan48/Wordle-Solver/blob/main/Statistica/solutii.txt)

<br/>

## Requirements
_Python 3.9_ 🐍   
[_PyGame_](https://www.pygame.org/wiki/GettingStarted)   &rarr;   `pip install pygame`

<br/>

## Instructions for Use:

### To play the game of Wordle &rarr; [wordle.py](https://github.com/Razvan48/Wordle-Solver/blob/main/Wordle/wordle.py)
```python
python wordle.py
```

### To run the solver &rarr; [solver.py](https://github.com/Razvan48/Wordle-Solver/blob/main/Solver/solver.py)
```python
python solver.py
```

<br/>

## Project Description

The project contains 2 main files ___solver.py___ and ___wordle.py___, which communicate using IPC (Inter-Process Communication).

When running ___solver.py___, the Wordle game will automatically open, where the solver's attempts to find the word chosen by the game will be sent. 
The solver starts by generating, with the help of entropy, the most favorable word and sends it to ___wordle.py___, and based on the feedback received, it narrows its search area, eliminating words that are not consistent with the feedback.

The received feedback consists of 5 characters which can be:
- ![#538D4E](https://placehold.co/15x15/538D4E/538D4E.png) &rarr; _V_  : the letter in that position is in the same position in the word to be guessed
- ![#B7A148](https://placehold.co/15x15/B7A148/B7A148.png) &rarr; _G_  : the letter is in the word, but in a different position
- ![#3A3A3C](https://placehold.co/15x15/3A3A3C/3A3A3C.png) &rarr; _N_  : the chosen word does not contain this letter

When running ___wordle.py___, the Wordle game opens, receiving information directly from the player. 
If the user enters a word that is not in the database, the squares will be colored red and a short animation will run.
After guessing the word, if the user presses the key ___"N"___, the game will restart with a new guess word without the need of closing and reopening the program.

<br/>

## References
- [PyGame Documentation](https://www.pygame.org/docs/)
- [Wordle](https://www.youtube.com/watch?v=v68zYyaEmEA&ab_channel=3Blue1Brown)


