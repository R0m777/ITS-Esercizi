'''Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica), 
salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."
'''

giorno:int = int(input("inserisci un giorno: "))
mese:int = int(input("inserisci numero del mese: "))
data = (giorno,mese)
match (giorno,mese):
        case (1,1):
            festività = "Capodanno"
        case (14,2):
            festività = "San valentino"
        case (15,8):
            festività = "Ferragosto"
        case (31,10):
            festività = "Halloween"
        case (25,12):
            festività = "Natale"
        case _:
            festività = "Nessuna festività importante in questa data."
   
if festività:
    print(f"il {giorno:02}/{mese:02} è {festività}")
else:
    print(f"{festività}")
   
    

