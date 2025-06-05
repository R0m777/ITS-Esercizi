'''Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold'''

def moltiplica(lista:list[int], threshold:int)-> int:
    risultato = 1
    for numero in lista:
        if numero < threshold:
            risultato = risultato * numero
    return risultato
    