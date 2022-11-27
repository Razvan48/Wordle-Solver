# Wordle Solver 
Primul proiect din cadrul cursului [Arhitectura Sistemelor de Calcul](https://cs.unibuc.ro/~crusu/asc/index.html)

<p>
  <img align = "left" width="400" height="533" src="https://github.com/sebimih13/Wordle-Solver/blob/main/gifs/player%20input.gif">
  <img align = "right" width="400" height="533" src="https://github.com/sebimih13/Wordle-Solver/blob/main/gifs/solver%20input.gif">
</p>

<br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br />


## Echipa

    1. Capatina Razvan Nicolae      - 152
    2. Mihalache Sebastian Stefan   - 152
    3. Petre-Soldan Adela           - 131

Numarul mediu de incercari pentru ghicirea tuturor cuvintelor  &rarr;  __4.91871835166754__  
Lantul incercarilor pentru fiecare cuvant din baza de date este scris in fisierul [__solutii.txt__](https://github.com/sebimih13/Wordle-Solver/blob/main/Statistica/solutii.txt)

<br />


## Requirements
_Python 3.9_ 🐍   
[_pygame_](https://www.pygame.org/wiki/GettingStarted)    &rarr;   `pip install pygame`

<br />


## Instructiuni de utilizare

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

Proiectul contine 2 fisiere principale ___solver.py___ si ___wordle.py___, care comunica prin IPC.  

La rularea ___solver.py___ se va deschide automat jocul wordle, unde vor fi trimise incercarile solver-ului de a gasi cuvantul ales de joc.  
Solver-ul incepe prin a genera cu ajutorul entropiei cel mai favorabil cuvant si il trimite catre ___wordle.py___, iar pe baza feedback-ului primit, isi restrange aria de cautare, eliminand cuvintele care nu sunt in concordanta cu feedback-ul.  

Feedback-ul primit este format din 5 caractere care pot fi:  
- ![#538D4E](https://placehold.co/15x15/538D4E/538D4E.png) &rarr; _V_  : litera de pe pozitia respectiva se afla pe aceeasi pozitie si in cuvantul care trebuie ghicit
- ![#B7A148](https://placehold.co/15x15/B7A148/B7A148.png) &rarr; _G_  : litera se afla in cuvant, dar pe alta pozitie
- ![#3A3A3C](https://placehold.co/15x15/3A3A3C/3A3A3C.png) &rarr; _N_  : cuvantul ales nu contine aceasta litera  

La rularea ___wordle.py___ se va deschide jocul wordle, care va primi informatii direct de la jucator.  
Daca user-ul introduce un cuvant care nu se afla in baza de date, patratele se vor colora cu rosu si se va genera o animatie de scurta durata.
Dupa ghicirea cuvantului, daca user-ul apasa tasta ___"N"___, jocul va reincepe cu un nou cuvant de ghicit fara a reporni programul.

<br />

## Referinte
- [pygame documentation](https://www.pygame.org/docs/)
- [wordle](https://www.youtube.com/watch?v=v68zYyaEmEA&ab_channel=3Blue1Brown)


