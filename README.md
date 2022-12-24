# Wordle Solver 
Primul proiect din cadrul cursului [Arhitectura Sistemelor de Calcul](https://cs.unibuc.ro/~crusu/asc/index.html)

<p>
  <img align = "left" width="400" height="533" src="https://github.com/sebimih13/Wordle-Solver/blob/main/gifs/player%20input.gif">
  <img align = "right" width="400" height="533" src="https://github.com/sebimih13/Wordle-Solver/blob/main/gifs/solver%20input.gif">
</p>

<br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br />


## Echipa

    1. Căpățînă Răzvan Nicolae      - 152
    2. Mihalache Sebastian Ștefan   - 152
    3. Petre-Șoldan Adela           - 131

Numărul mediu de incercări pentru ghicirea tuturor cuvintelor  &rarr;  __4.91871835166754__  
Lanțul încercărilor pentru fiecare cuvânt din baza de date este scris in fișierul [__solutii.txt__](https://github.com/sebimih13/Wordle-Solver/blob/main/Statistica/solutii.txt)

<br />


## Requirements
_Python 3.9_ 🐍   
[_pygame_](https://www.pygame.org/wiki/GettingStarted)    &rarr;   `pip install pygame`

<br />


## Instrucțiuni de utilizare

### Pentru a juca Wordle &rarr; [wordle.py](https://github.com/sebimih13/Wordle-Solver/blob/main/Wordle/wordle.py)
```python
python wordle.py
```

### Pentru a rula solver-ul &rarr; [solver.py](https://github.com/sebimih13/Wordle-Solver/blob/main/Solver/solver.py)
```python
python solver.py
```

<br />


## Descrierea proiectului

Proiectul conține 2 fișiere principale ___solver.py___ și ___wordle.py___, care comunica prin IPC.  

La rularea ___solver.py___ se va deschide automat jocul wordle, unde vor fi trimise încercările solver-ului de a găsi cuvântul ales de joc.  
Solver-ul începe prin a genera cu ajutorul entropiei cel mai favorabil cuvânt si îl trimite către ___wordle.py___, iar pe baza feedback-ului primit, își restrânge aria de căutare, eliminând cuvintele care nu sunt in concordanță cu feedback-ul.  

Feedback-ul primit este format din 5 caractere care pot fi:  
- ![#538D4E](https://placehold.co/15x15/538D4E/538D4E.png) &rarr; _V_  : litera de pe poziția respectivă se află pe aceeași poziție și în cuvântul care trebuie ghicit
- ![#B7A148](https://placehold.co/15x15/B7A148/B7A148.png) &rarr; _G_  : litera se află în cuvânt, dar pe altă poziție
- ![#3A3A3C](https://placehold.co/15x15/3A3A3C/3A3A3C.png) &rarr; _N_  : cuvântul ales nu conține această literă 

La rularea ___wordle.py___ se va deschide jocul wordle, care va primi informații direct de la jucător.  
Dacă user-ul introduce un cuvânt care nu se află în baza de date, pătratele se vor colora cu roșu si se va genera o animație de scurtă durată.
După ghicirea cuvântului, dacă user-ul apasă tasta ___"N"___, jocul va reîncepe cu un nou cuvânt de ghicit fără a reporni programul.

<br />

## Referințe
- [pygame documentation](https://www.pygame.org/docs/)
- [wordle](https://www.youtube.com/watch?v=v68zYyaEmEA&ab_channel=3Blue1Brown)


