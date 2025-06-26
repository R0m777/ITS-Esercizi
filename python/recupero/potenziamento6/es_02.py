'''
Scrivere un programma in Python che legga dall’utente una serie di nomi di persona (stringhe). 
L'inserimento dei nomi deve terminare quando l’utente inserisce un nome già inserito in precedenza, oppure sono stati inseriti 30 nomi distinti. 
Inoltre, si deve porre il vincolo che ciascun nome sia una stringa di lunghezza inferiore a 20 caratteri e che non venga inserita una stringa vuota.

Al termine dell'inserimento, il programma deve:
- stampare quanti nomi sono stati inseriti in totale;
- stampare il nome più lungo tra quelli inseriti;
- stampare la lunghezza del nome più lungo.

Se ci sono più nomi con la stessa lunghezza massima, puoi scegliere uno qualsiasi tra quelli più lunghi.

Esempio:
Inserisci un nome: Dora
Inserisci un nome: Marcella
Inserisci un nome: Teresa
Inserisci un nome: Valentina
Inserisci un nome: Dora
 
Hai inserito 4 nomi distinti.
Il più lungo è Valentina con 9 caratteri.
'''


nomi = []
while True:
    nome = input("Inserisci un nome: ").strip()
        

    if nome == "":
        print("Errore: il nome non può essere una stringa vuota.")
        continue
        
        
    if len(nome) >= 20:
        print("Errore: il nome deve essere più corto di 20 caratteri.")
        continue
        
    if nome in nomi:
        break
    else:
        nomi.append(nome)
        
   
    if len(nomi) == 30:
            break
    
    if nomi:
        nome_lunogo = max(nomi)
         
        print(f"\nHai inserito {len(nomi)} nomi distinti.")
        print(f"Il più lungo è {nome_lunogo} con {len(nome_lunogo)} caratteri.")
    else:
        print("Non è stato inserito alcun nome valido.")



    

