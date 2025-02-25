'''Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, e
ntrambe contenenti valori interi, 
calcoli la somma incrociata degli elementi.
'''
#input
n:int = int(input("Inserisci la lunghezza delle liste: "))
a:int = [int(input(f"Inserisci elemento {i+1} di a: ")) for i in range(n)]
b:int = [int(input(f"Inserisci elemento {i+1} di b: ")) for i in range(n)]

c:int = [a[i] + b[n - 1 - i] for i in range(n)] #nuova lista per salvare la somma degli elementi delle liste a,b

#output
print("Lista a:", a)
print("Lista b:", b)
print("Lista c:", c)
