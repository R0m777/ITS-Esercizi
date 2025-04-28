'''Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.'''

def sum_above_threshold(numbers: list[int], threshold) -> int:
    sum = 0
    for n in numbers:
        if n > threshold:
            sum = sum+n
            return sum
        

print(sum_above_threshold([15, 5, 25], 20))