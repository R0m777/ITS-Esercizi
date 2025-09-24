from film import Film
from __future__ import annotations

class Azione(Film):
    __genere: str
    __penale: float

    def __init__(self, penale: float):
        self.__genere = "Azione"
        self.__penale = penale

    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni_ritardo: int) -> float:
        if giorni_ritardo > 0:
            penale_calcolata = giorni_ritardo * 3.0
            self.__penale = penale_calcolata 
            return penale_calcolata
        else:
            return 0.0 





class Commedia(Film):
    __genere: str
    __penale: float

    def __init__(self, penale: float):
        self.__genere = "Commedia"
        self.__penale = penale

    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni_ritardo: int) -> float:
        if giorni_ritardo > 0:
            penale_calcolata = giorni_ritardo * 3.50
            self.__penale = penale_calcolata 
            return penale_calcolata
        else:
            return 0.0 



class Dramma(Film):
    __genere: str
    __penale: float

    def __init__(self, penale: float):
        self.__genere = "Dramma"
        self.__penale = penale

    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni_ritardo: int) -> float:
        if giorni_ritardo > 0:
            penale_calcolata = giorni_ritardo * 2.0
            self.__penale = penale_calcolata 
            return penale_calcolata
        else:
            return 0.0 