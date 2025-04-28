'''Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. 
Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.
Scrivere un programma che:

Acquisisca in input un valore N (numero di euro disponibili).
Calcoli e mostri in output il numero totale di barrette che si possono ottenere, 
considerando anche quelle ottenute con i buoni sconto.
Mostri quanti buoni sconto avanzano al termine dell'acquisto.

Esempio:
Se l'utente inserisce N = 6, può acquistare 6 barrette ottenendo 6 buoni sconto, 
che gli permettono di riscattare 1 ulteriore barretta gratuita, per un totale di 7 barrette. Alla fine, non rimarranno buoni sconto inutilizzati.

Il programma deve continuare a scambiare i buoni con nuove barrette finché ce ne sono abbastanza per ottenere almeno una barretta gratuita.'''

#input
n:int = int(input("Inserisci il numero di euro disponibili: "))
buoni = n
barrette = n
barrette_gratis = 0

#condizione
while buoni>=6:                    
    barrette_gratis = buoni // 6
    barrette+=barrette_gratis
    buoni = buoni % 6 
 
    
#output
print(f"Numero totale di barrette ottenute: {barrette}")
print(f"Buoni sconto avanzati: {buoni}")
