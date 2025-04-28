'''Scrivere un programma in Python che utilizzi un match statement per classificare un voto scolastico in base alla scala italiana.
Il programma deve accettare in input un voto numerico intero da 1 a 10 e stampare la valutazione corrispondente:

- 10 → "Eccellente"
- 8-9 → "Molto buono"
- 6-7 → "Sufficiente"
- 4-5 → "Insufficiente"
- 1-3 → "Gravemente insufficiente"
- Altro caso → "Voto non valido"'''

n:int = int(input("Inserire il voto: "))
match n:
    case 10:
        print("Eccellente!")
    case 9|8:
        print("Molto buono!")
    case 7|6:
        print("Sufficente")
    case 5|4:
        print("Insufficente")
    case n if n > 0 and n < 4:
        print("Gravemente insufficente")
    case _:
        print("Voto non valido")
