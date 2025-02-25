'''Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall'utente.

Il programma deve:

    acquisire una sequenza di numeri interi, terminando l'inserimento quando l'utente digita 0 (che non deve essere considerato nei calcoli);
    calcolare e visualizzare la somma di tutti i numeri pari inseriti;
    calcolare e visualizzare la media di tutti i numeri dispari inseriti;
    determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
    se più numeri hanno la stessa frequenza massima, visualizzarli tutti.
'''

numeri:list = []
#input
print("Inserisci numeri interi (0 per terminare):")

while True:
    n:int = int(input())  
    if n == 0:
        break
    numeri.append(n)    #aggiungere n alla lista numeri

if len(numeri) > 0:     #verifica se ci sono valori n nella lista numeri
    somma_pari = 0      #variabile somma numeri pari
    somma_dispari = 0   #variabile somma numeri dispari
    conta_dispari = 0   #contatore dei numeri dispari
    frequenze:dict = {}      
    
    for numero in numeri:
        if numero % 2 == 0:
            somma_pari += numero
        else:
            somma_dispari += numero
            conta_dispari += 1
        
        if numero in frequenze:
            frequenze[numero] += 1
        else:
            frequenze[numero] = 1
    
    media_dispari = somma_dispari / conta_dispari if conta_dispari > 0 else 0
    massima_frequenza = max(frequenze.values())  #La funzione max viene utilizzata per trovare il valore massimo di un oggetto iterabile.
    numeri_piu_frequenti:list = []  #lista per slvare i valori piu frequenti
    
    for num, freq in frequenze.items():
        if freq == massima_frequenza:
            numeri_piu_frequenti.append(num)
    
    #output
    print("Somma dei numeri pari:", somma_pari)
    print("Media dei numeri dispari:", media_dispari)
    print("Numero/i con frequenza più alta:", ", ".join(str(num) for num in numeri_piu_frequenti))
else:
    print("Nessun numero valido inserito.")

