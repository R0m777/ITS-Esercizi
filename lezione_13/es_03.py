'''Il fattoriale di un intero non negativo n, scritto n!, è il prodotto

n * (n-1) * (n-2) * ... * 1

con 1! uguale a 1 e 0! definito come 1.
Si scriva una funzione ricorsiva recursiveFactorial che dato un numero n calcoli n!.
 '''

def Nfattoriale(n:int)-> int:
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return "Errore"    
    else:
        return int(n*Nfattoriale(n-1))
    
print(Nfattoriale(5))
print("-"*30)
print(Nfattoriale(-5))
print("-"*30)
print(Nfattoriale(1))