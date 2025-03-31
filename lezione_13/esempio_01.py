def recursivSum(n:int) -> int:
    # n is negative
    if n < 0:
       print("Errore!")
       return 0
    # n = o
    elif n == 0:
        return 0
    # n è positivo, calcola la somma
    else:
        return int(n + recursivSum(n-1)) 

print(recursivSum(5))
print("-" *30)
print(recursivSum(-5))