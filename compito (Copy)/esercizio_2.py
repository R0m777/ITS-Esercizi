'''Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa. 
Il risultato deve essere visualizzato in output.'''

#input
testo:str = str(input("Inserisci una stringa: "))

numero_spazi:int = testo.count(" ")

#output
print(f"Il numero totale di spazi presenti nella stringa: {numero_spazi}")
