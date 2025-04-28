'''Scrivere un programma che permetta all'utente di inserire una serie di parole in input, 
terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, 
il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.'''

#input
while True:
    parola:str = str(input("Inserisci una parola (digita 'fine' per terminare): "))
        
    if parola.lower() == "fine":       #.lower serve per terminare il programma quando si digita FINE in maiuscolo
        break
        
    if len(parola) > 1 and parola[0] == parola[-1]:
        #output
        print(f"La parola '{parola}' inizia e finisce con lo stesso carattere.")
    else:
        print(f"La parola '{parola}' non inizia e finisce con lo stesso carattere.")
