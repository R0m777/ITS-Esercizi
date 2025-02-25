'''Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). 
L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.

Il programma deve:

Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).
'''

numeri:list = []
numeri_interi:list = []
#input    
while True:
        n = float(input("Inserisci un numero positivo (negativo per terminare): "))
        if n < 0:
            break
        numeri.append(n)
        if n.is_integer():                       #is_integer serve per verificare se il numero inserito è intero
            numeri_interi.append(int(n))

    
        if numeri:
            max_n = max(numeri)
            min_n = min(numeri)
            #output
            print(f"Numero massimo inserito: {max_n}")
            print(f"Numero minimo inserito: {min_n}")
        else:
            print("Nessun numero valido inserito.")
    
        if numeri_interi:
           media_interi = sum(numeri_interi) / len(numeri_interi)
           #output
           print(f"Media dei numeri interi: {media_interi}")
        else:
           print("Nessun numero intero inserito, impossibile calcolare la media.")

