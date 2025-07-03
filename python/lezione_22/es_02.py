from __future__ import annotations
from abc import ABC, abstractmethod


class CodificatoreMessagio(ABC):

    @abstractmethod
    def codifica(self, testolnChiaro):
        pass


class DecodificatoreMessagio(ABC):

    @abstractmethod
    def decodifica(self, testoCodificato):
        pass


class CifratoreAScorrimento(CodificatoreMessagio, DecodificatoreMessagio):
    def __init__(self, chiave:int):
        self.chiave = chiave 
        self.alfabeto_maiuscolo = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.alfabeto_minuscolo = list("abcdefghijklmnopqrstuvwxyz")

    def __sposta_carattere(self, c):
        if c in self.alfabeto_minuscolo:
            idx = self.alfabeto_minuscolo.index(c)
            nuovo_idx = (idx + self.chiave) % 26
            return self.alfabeto_minuscolo[nuovo_idx]
        elif c in self.alfabeto_maiuscolo:
            idx = self.alfabeto_maiuscolo.index(c)
            nuovo_idx = (idx + self.chiave) % 26
            return self.alfabeto_maiuscolo[nuovo_idx]
        return c

    def __decodifica_carattere(self, c):
        if c in self.alfabeto_minuscolo:
            idx = self.alfabeto_minuscolo.index(c)
            nuovo_idx = (idx - self.chiave) % 26
            return self.alfabeto_minuscolo[nuovo_idx]
        elif c in self.alfabeto_maiuscolo:
            idx = self.alfabeto_maiuscolo.index(c)
            nuovo_idx = (idx - self.chiave) % 26
            return self.alfabeto_maiuscolo[nuovo_idx]
        return c

    def codifica(self, testoInChiaro:str) -> str:
        return ''.join(self.__sposta_carattere(c) for c in testoInChiaro)
    
    def decodifica(self, testoCodificato:str) -> str:
        return ''.join(self.__decodifica_carattere(c) for c in testoCodificato)
'''
class CiftaroreACombinazione(CodificatoreMessagio, DecodificatoreMessagio):
    def __init__(self, n:int):
        self.n = n

    def codifica(self, testolnChiaro:str) -> str:
        super().codifica(testolnChiaro)
        testo = testolnChiaro
        for i in range(self.n):
            testo = self.__combinazione(testo)
        return testo
    

    def __combinazione(self, testo: str) -> str:
        mid = len(testo)// 2 
        prima_meta = testo[:mid]
        seconda_meta = testo[mid:]
        risultato = []
     
        for i in range(len(seconda_meta)):
            risultato.append(prima_meta[i])
            risultato.append(seconda_meta[i])
        return risultato
    '''
    
def test_cifratore_a_scorrimento():
    print("Esecuzione test: CifratoreAScorrimento")

    chiave = 3
    cifratore = CifratoreAScorrimento(chiave)

    messaggio = "Ciao Mondo!"
    atteso_codificato = cifratore.codifica(messaggio)
    atteso_decodificato = cifratore.decodifica(atteso_codificato)

    print("Messaggio originale:", messaggio)
    print("Messaggio codificato:", atteso_codificato)
    print("Messaggio decodificato:", atteso_decodificato)
    print("Test passato:", messaggio == atteso_decodificato)

test_cifratore_a_scorrimento()

'''
# Test combinazione
c2 = CifratoreACombinazione(2)
msg2 = "abcdefghi"
c2_cod = c2.codifica(msg2)
c2_dec = c2.decodifica(c2_cod)

print("\nCombinazione:")
print("Codificato:", c2_cod)
print("Decodificato:", c2_dec)
'''






