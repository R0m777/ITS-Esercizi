'''Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi.
 Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.'''

def count_isolated(lista:list[int]) -> int:
    for i in range(len(lista)):
        print(count_isolated([1, 2, 2, 3, 3, 3, 4]))

print(count_isolated([1, 2, 3, 4, 5]))