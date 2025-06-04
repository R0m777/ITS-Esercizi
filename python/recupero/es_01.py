'''1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
Se la chiave è già presente, 
somma il valore al valore già associato alla chiave.'''

def lista(tupla_lista:list[tuple]) -> dict:
    dizionario = {}
    for key, value in tupla_lista:
        if key in dizionario:
            dizionario[key] += value
        else:
            dizionario[key] = value
    return dizionario






        





