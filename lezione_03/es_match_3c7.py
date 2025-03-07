'''Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".

NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.'''

testa = []
croce = []

for i in range(8):
    while True:
            x:str = str(input(f"{i+1} inserisce t o T se è uscito testa, mentre inserisce c o C se è uscito croce: ")).lower()
            break
        
    match x:
           case "t" | "T":
               testa.append(x)
           case "c" | "C":
               croce.append(x)
           case _:
              print("lancio non valido")
              

print(f"Totale testa: {len(testa)}\nTotale croce: {len(croce)}")
import math
percentuale_t = len(testa) / 8 * 100
percentuale_c = len(croce) / 8 * 100
print(f"percentuale testa: {percentuale_t}")
print(f"percentuale croce: {percentuale_c}")

