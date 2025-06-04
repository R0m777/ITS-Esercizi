'''Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.'''

def classifica_numeri(lista_numeri:list)-> dict:
    risultato:dict[str, list] = {
        "positivi": [],
        "negativi": []
    }

    for numero in lista_numeri:
        if numero >= 0:
            risultato["positivi"].append(numero)
        else:
            risultato["negativi"].append(numero)

    return risultato


numeri = [3, -1, 0, 7, -5, 2, -3]
print(classifica_numeri(numeri))

