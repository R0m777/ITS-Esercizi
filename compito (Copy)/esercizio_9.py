'''Il valore di π può essere approssimato utilizzando la seguente serie infinita:

π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini sono necessari per ottenere approssimazioni sempre più accurate. 
Quindi:

progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.

Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.'''

thresholds:float = [3.14, 3.141, 3.1415, 3.14159]
results:dict = {}

for threshold in thresholds:
    pi_approssimato = 0  # Valore approssimato di π
    denominatore = 1  # Denominatore iniziale
    term_count = 0  # Conteggio dei termini
    
    while round(pi_approssimato, len(str(threshold))-2) != threshold:
        term_count += 1
        if term_count % 2 == 1:
            pi_approssimato += 4 / denominatore  # Aggiunge il termine se dispari
        else:
            pi_approssimato -= 4 / denominatore  # Sottrae il termine se pari
        denominatore += 2  # Incrementa il denominatore di 2
    
    results[threshold] = term_count

for value, terms in results.items():
    #output
    print(f"Per ottenere π ≈ {value}, sono necessari {terms} termini.") 








