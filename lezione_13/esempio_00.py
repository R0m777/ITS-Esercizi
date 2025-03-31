import time

def recursivCountdown(n:int) -> None:
    # n è negativo
    if n < 0:
        print("Errore!")

    # n = 0 interrompe la funzione
    elif n == 0:
        print(0)
    
    # altri casi
    else:
        time.sleep(1)
        print(n)
        recursivCountdown(n-1)
        

recursivCountdown(5)
print("-" *30)
recursivCountdown(0)
print("-" *30)
recursivCountdown(-5)