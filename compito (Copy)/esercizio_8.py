'''Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) e visualizzi in output un grafico a barre testuale con asterischi *.

Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.'''

numeri:list = []
#input
for i in range(5):
    while True:
        
            n:int = int(input(f"Inserisci il numero {i+1} compreso tra 1 e 30: "))
            if 1 <= n <= 30:
                numeri.append(n)
                break
            else:
                print("Errore: inserisci un numero compreso tra 1 e 30.")
        
#output
print("\nGrafico a barre:")
for n in numeri:
    print("*" * n)