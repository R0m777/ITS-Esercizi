'''Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, 
inclusi gli estremi.
Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.'''

#input
n1:int = int(input("Inserisci il primo numero intero: "))
n2:int = int(input("Inserisci il secondo numero intero: "))
    
if n1 > n2:
    n1, n2 = n2, n1
    
    prodotto = 1                             #variabile per salvare il prodotto
    for numero in range(n1, n2 + 1):
        prodotto *= numero
    #output
    print(f"Il prodotto dei numeri tra {n1} e {n2} (inclusi) è: {prodotto}")

elif n2 > n1:
    n2, n1 = n1, n2

    prodotto = 1
    for numero in range(n2, n1 + 1):
        prodotto *= numero
    #output    
    print(f"Il prodotto dei numeri tra {n2} e {n1} (inclusi) è: {prodotto}")

else:
    print(f" il prodotto dei numeri {n1} e {n2} è: {n1 * n2}")



