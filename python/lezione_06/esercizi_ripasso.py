def inverti_mappa(dizionario:dict[str:int])->dict[int:str]:
    risultato = {}
    for key, value in dizionario.items():
        if value not in risultato:
            risultato[value] = key
    return risultato
print(inverti_mappa({'a': 1, 'b': 2, 'c': 3}))
print(inverti_mappa({}))

'''Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.'''

def rimuovi_elementi(lista:list, dizionario:dict[int:int])->dict:
    risultato = lista.copy()
    for elemento , count in dizionario.items():
        for i in range(count):
            if elemento in risultato:
                risultato.remove(elemento)
            else:
                break
    return risultato

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))

'''Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.'''

def aggrega_voti(voti: list[dict])-> dict[str:list[int]]:
    aggregato = {}
    for record in voti:
        nome = record["nome"]
        voto = record["voto"]
        if nome not in aggregato:
            aggregato[nome] = []
        aggregato[nome].append(voto)
    return aggregato

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))