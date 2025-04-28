'''Scrivere un programma in Python che legga una frase di una riga e mostri una delle seguenti risposte:
- "Si" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è pari;
- "No" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è dispari;
- "Wow!" -> se la frase termina con un punto esclamativo (!)
- "Tu dici" seguito dalla frase inserita racchiusa tra doppi apici in tutti gli altri casi.
'''

frase:str = str(input("Inserisci una frase: "))

if frase.endswith("?"):
       if len(frase) % 2 == 0:
        print("SI")
       else:
            print("NO")
elif frase.endswith("!"):
     print("WOW!")
else:
     print(f"Tu Dici: {frase}")



