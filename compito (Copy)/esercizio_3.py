'''Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale. 
Il programma deve poi visualizzare la stringa ottenuta in output. 
Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.'''

#input
stringa:str = str(input("Inserisci una stringa: "))
stringa_invertita:str = stringa[::-1]

for i in range(len(stringa)):
    #output
    print(f"Stringa invertita: {stringa_invertita}")
    break


