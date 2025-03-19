'''Scrivi una funzione che unisce due dizionari. 
Se una chiave è presente in entrambi, somma i loro valori.'''

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict0:dict = dict1.copy()
    for key , values in dict2.items():
        dict0[key] = dict0.get(key,0) + values
    return dict0





print(merge_dictionaries({'x': 5}, {'x': -5}))
print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

	

