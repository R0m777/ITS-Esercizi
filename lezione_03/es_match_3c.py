'''Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, 
espresso come numero intero e usare un match per determinare il corrispondente GPA americano, secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valido"'''

n = input("Inserisci un voto: ")
if n == n.isnumeric():

   match n: 
    case n if n >= 106 and n <= 110:
        print("4.0")
    case n if n >= 101 and n <= 105:
        print("3.7")
    case n if n >= 96 and n <= 100:
        print("3.3")
    case n if n >= 91 and n <= 95:
        print("3.0")
    case n if n >= 86 and n <= 90:
        print("2.7")
    case n if n >= 81 and n <= 85:
        print("2.3")
    case n if n >= 76 and n <= 80:
        print("2.0")
    case n if n >= 70 and n <= 75:
        print("1.7")
    case n if n >= 66 and n <= 69:
        print("1.0")

else:
    print("Voto non valido")
        


