'''Creare in Python una lista vuota chiamata 'oggetti'. Con un ciclo, riempire questa lista con tre oggetti diversi.
Scrivere, poi, un programma che utilizzi un match statement per classificare gli oggetti presenti nella lista:

- ["penna", "matita", "quaderno"] → "Materiale scolastico"
- ["pane", "latte", "uova"] → "Prodotti alimentari"
- ["sedia", "tavolo", "armadio"] → "Mobili"
- ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
- Qualsiasi altra lista → "Categoria sconosciuta"'''

oggetti:set = []

for i in range(3):
    while True:
       n = str(input(f"Inserisci elemnto {i+1} : ")).lower()
       oggetti.add(n)
       break
       
match oggetti:
    case ["penna", "matita", "quaderno"]:
        print(f"{oggetti}\nMateriale scolastico")
    case ["pane", "latte", "uova"]:
        print("Prodotti alimentari")
    case ["armadio", "sedia", "tavolo"]:
        print("Mobili")
    case ["telefono", "compiuter", "tablet"]:
        print("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")
