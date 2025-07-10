import random
from __future__ import annotations

class Creatura:
    _name: str
    def __init__(self, name:str) -> None:
        self.setNome(name)

    def setNome(self, name) -> None:
        if isinstance(name, str):
            self._name = name
        else:
            self._name = "Creatura Generica"

    def getNome(self) -> str:
        return self._name
    
    def __str__(self) -> str:
        return f"Creatura: {self._name}"
    
class Alieno(Creatura):
    _matricola:int
    _munizioni:int
    def __init__(self):
        
        super().__init__()
        self._setMatricola()
        self._setMunizioni()

        nome_alieno = f"Robot-{self._matricola}"
        if not self.getNome().startswith("Robot-") or self.getNome() != nome_alieno:
            print("Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!.")
        self.setNome(nome_alieno)

    def _setMatricola(self)-> None:
        self._matricola = random.randint(10000, 90000)

    def _setMunizioni(self)-> None:
        self._munizioni = [i**2 for i in range(15)]

    def getMatricola(self) -> int:
        return self._matricola
    
    def getMunizioni(self) -> list[int]:
        return self._munizioni
    
    def __str__(self) -> str:
        return f"Alieno: {self.getNome()}"
    
class Mostro(Creatura):
    def __init__(self, urlo_vittoria:str, gemito_sconfitta:str, assalto:list[int]):
        super().__init__()
        self.setVittoria(urlo_vittoria)
        self.setSconfitta(gemito_sconfitta)
        self._setAssalto(assalto)

    def _setAssalto(self) -> None:
        self.assalto = random.sample(range(1, 101), 15)

    def setVittoria(self, vittoria) -> None:
        if isinstance(vittoria, str):
            self.urlo_vittoria = vittoria
        else:
            self.urlo_vittoria = "GRAAAHHH"

    def setSconfitta(self, sconfitta)-> None:
        if isinstance(sconfitta, str):
            self.gemito_sconfitta = sconfitta
        else:
            self.gemito_sconfitta = "Uuurghhh"

    def getUrloVittoria(self) -> str:
        return self.urlo_vittoria
    
    def getGemitoSconfitta(self):
        return self.gemito_sconfitta

    def getAssalto(self):
        return self.assalto

    def __str__(self):
        name = self.getNome()
        new_name = ""

        for i, in range(len(name)):
            char = name[i]
            if i % 2 == 0:
                new_name += char.lower()
            else:
                new_name += char.upper()
        return f"Mostro: {new_name}"


    
