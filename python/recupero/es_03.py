'''Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.'''

def diz_prodotti(dizionario:dict) -> dict:
    diz_nuovo:dict = {}
    for key, values in dizionario.items():
        if values < 50:
            values = round(values * 1.10, 2)
            diz_nuovo[key] = values
    return diz_nuovo

prodotti = {
    "pane": 40,
    "latte": 60,
    "uova": 30
}

print(diz_prodotti(prodotti))

