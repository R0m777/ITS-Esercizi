from __future__ import annotations

class Studente:
    _nome: str #mutabile noto alla nascita
    _modulo: set[Modulo]
    _esami: set[Esame] # certamente non noto alla nascita
    
    def __init__(self, nome:str) -> None:
        self.set_nome(nome)
        self._modulo = set()
        self._esami = {}

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def modulo(self) -> frozenset[Modulo]:
        return frozenset(self._modulo)
    
    def esami(self) -> frozenset[Esame]:
        return frozenset(self._esami)
    
    def add_esame(self, modulo: Modulo, voto: int) -> None:
        new_esame: Esame = Esame(studente=self, modulo=modulo, voto=voto)

        if new_esame in self._esami:
            raise RuntimeError(f" lo stdente {self.nome()} ha già superato un esame di {modulo.codice()}")
        self._esami.add(new_esame)

    def remove_link_esame(self, esame:Esame) -> None:
        self._esami.remove(esame)

    def remove_esame(self, modulo: Modulo)->None:
        for esame in self.esami():
            if esame.modulo() == modulo:
                self.remove_link_esame(esame)
                return
        raise ValueError(f"impossibile rimuovere l'esame {modulo.codice()} perchè {self.nome()} non l'ha sostenuto")

    def media_voti(self) -> float:
        if len(self._esami) == 0:
            raise RuntimeError
        
        return sum(self._esami.values()) / len(self._esami)


class Modulo:
    _codice:str #immutabile noto alla nascita
    def __init__(self, codice:str) -> None:
        self.set_codice(codice)

    def codice(self) -> str:
        return self._codice
    
    def set_codice(self, codice:str) -> None:
        self._codice = codice
    
class Esame:
    _studente: Studente
    _modulo: Modulo
    _voto: int

    def __int__(self, studente:Studente, modulo:Modulo, voto:int) -> None:
        self._studente = studente # immutabile ()
        self._modulo = modulo # immutabile
        self._voto = voto # immutabile

    def studente(self) -> Studente:
        return self._studente
    
    def modulo(self) -> Modulo:
        return self._modulo
    
    def voto(self) -> int:
        return self._voto
    
    def __repr__(self) -> str:
        return f"Esame({self.studente().nome()}, {self.modulo().codice()}: {self.voto()})"
    


'''prog1 = Modulo("progettazione")

alice = Studente("Alice")

alice.add_esame(modulo=prog1, voto=28)
max([e.voto() for e in alice.esami()])

print(alice)'''

alice = Studente("Alice")
biagio:Studente = Studente("Biagio")

prog1: Modulo = Modulo("prog.1")
python14:Modulo = Modulo("python14")
web12:Modulo = Modulo("Web12")

alice.add_esame(modulo=prog1, voto=28)
alice.add_esame(modulo=python14, voto=29)

alice.remove_esame(prog1)

try:
    alice.add_esame(modulo=python14, voto=31)
except AttributeError:
  print(f" {alice.nome()}, {python14.codice}")

esami_alice = alice.esami()
print(f"{alice.nome()} ha superato {len(esami_alice)} esami")

alice.add_esame(modulo=web12, voto=19)
media_alice: float = alice.media_voti()
print(f"la media voti di alice è {media_alice}")
