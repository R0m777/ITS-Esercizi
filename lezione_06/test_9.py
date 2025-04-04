'''Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, 
ritorni un nuovo insieme senza i numeri specificati nella lista.'''

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    return original_set - set(elements_to_remove)

print(remove_elements({5, 6, 7}, [7, 8, 9]))
print(remove_elements({1, 2, 3, 4}, [2, 3]))
print(remove_elements({1, 2}, [3]))
print(remove_elements(set(), [1, 2, 3]))
print(remove_elements({10, 20, 30}, []))