from abc import ABC, abstractmethod
from __future__ import annotations

class Volo(ABC):
    def __init__(self, codice_volo: str, capacita_massima: int):
        self.codice_volo = codice_volo
        self.capacita_massima = capacita_massima
        self.prenotazioni = 0  

    @abstractmethod
    def prenota_posto(self, posti:int, classe_servizio:str) -> str:
        pass

    @abstractmethod
    def posti_disponibili(self):
        pass

    
class VoloCommerciale(Volo):
    def __init__(self, codice_volo, capacita_massima):
        super().__init__(codice_volo, capacita_massima)
    
        self.posti_economica = int(self.capacita_massima * 0.7)
        self.posti_business = int(self.capacita_massima *0.2)
        self.posti_prima = self.capacita_massima - (self.posti_economica + self.posti_business)

        self.prenotazioni_economica = 0
        self.prenotazioni_business = 0
        self.prenotazioni_prima = 0

    def posti_disponibili(self) -> dict:
        posti_disp_economica = self.posti_economica - self.prenotazioni_economica
        posti_disp_business = self.posti_business - self.prenotazioni_business
        posti_disp_prima = self.posti_prima - self.prenotazioni_prima

        

        return {
            'posti disponibili': self.capacita_massima,
            'classe economica': posti_disp_economica,
            'classe business': posti_disp_business,
            'prima classe': posti_disp_prima
        }