# Wordle-Solver
## Proiect Arhitectura sistemelor de calcul

### Echipa:

    1.Capatina Razvan Nicolae, 152
    2.Mihalache Sebastian, 152
    3.Petre-Soldan Adela, 131

Numarul mediu de incercari pentru ghicirea tuturor cuvintelor: 4.91871835166754

### Descirerea proiectului:

Proiectul contine 2 fisiere principale, "solver.py" si "wordle.py", care comunica prin IPC.
Solver-ul incepe prin a genera cu ajutorul entropiei cel mai favorabil cuvant ("bestWord") si il trimite catre wordle.py prin functia
"sendBestWord()", iar pe baza feedback-ului primit inapoi prin functia "receiveFeedback()" isi restrange aria de cautare, eliminand
cuvintele care nu sunt in concordanta cu feedback-ul.
Feedback-ul primit este format din 5 caractere care pot fi 'V' (verde), 'G'(galben) sau 'N' (negru). Verde inseamna ca litera de pe pozitia
respectiva se afla
pe aceeasi pozitie si in cuvantul care trebuie ghicit ("hiddenWord"), galben inseamna ca litera se afla in hiddenWord dar pe alta pozitie, iar negru
inseamna ca nu se gadeste deloc.
Pentru a modifica viteza cu care sunt afisate cuvintele pe ecran, s-a folosit variabila "canReadWrite" care se activeaza pentru o singura iteratie
la o anumita perioada de timp. 
Solver-ul trimite "bestWord-ul" printr-un singur mesaj, dar fiecare litera este afisata pe rand cu ajutorul variabilei "indexSolver" care se modifica
la fiecare iteratie in care variabila "canReadWrite" este activa.

Solver-ul se opreste atunci cand feebdack-ul pe care il primeste este "VVVVV", adica atunci cand cuvantul a fost gasit.

Daca valoarea din "gameMode.txt" este 0, inseamna ca utilizatorul va juca in locul inteligentei artificiale, iar solver-ul nu mai este rulat.
Daca user-ul introduce un cuvant care nu se afla in baza de date, patratele se vor colora cu rosu in loc de verde, galben sau negru
si se va genera o animatie de scurta durata prin care randul respectiv se depaseaza succesiv la stanga si la dreapta. 
Dupa ghicirea cuvantului, daca user-ul apasa tasta "N", jocul va reincepe cu un nou cuvant de ghicit fara a rula din nou programul.

Media incercarilor a fost calculata prin parcurgerea intregii baze de date si rularea codului pentru fiecare cuvant. 
Pentru a grabi procesul, fisierul "sol.py" contine o clasa cu functiile esentiale pentru ghicirea cuvantului, fara sa se
mai tina cont de interfata grafica (creata cu ajutorul functiilor bibliotecii "pygame").
Media este stocata in fisierul "medie.txt", iar lantul incercarilor pentru fiecare cuvant in fisierul "metodaCuvinte.txt" .

### Referinte:

