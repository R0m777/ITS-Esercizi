def sumInRange(a:int, b:int) -> int:
    # if a > b, swap i valori di a e b
    if a > b:
        # creo una variabile per salvare il valore di a
        temp:int = a
        # scambio a e b
        a = b
        # adesso b = a
        b = temp
    # if b = a, si ferma il processo
    if b == a:
        return int(a)
    # in altri casi si fa la somma
    else:
        return int(b + sumInRange(a,b-1))
    
print(sumInRange(0,-5))
print("-"*30)
print(sumInRange(2,2))
print("-"*30)
print(sumInRange(8,3))