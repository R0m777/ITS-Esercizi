from Lezione_08.morfismo.persona import Persona


class Studente(Persona):
    # Inizializzare un oggetto della classe Studente
    def __init__(self, name: str, last_name: str, age: int, matricola: str):
        # Inizializzare la superclasse
        super().__init__(name, last_name, age)
        # Inizializzare l'attributo matricola
        self.setMatricola(matricola)

    # Metodo setter per l'attributo matricola
    def setMatricola(self, matricola: str) -> None:
        if matricola:
           self.matricola = matricola
        else:
            print("Errore")

    # un metordo per visualizzare le info relative alla classe Studente
    def getMatricola(self) -> str:
        return self.matricola
    
    def __str__(self)->str:
        return f"\nNome: {self.getName()}\nCongnome: {self.getLast_name()}\nMatricola: {self.getMatricola()}"
    
    # metodo che mi consente di calcolare la media degli esami sostenuti da uno studente
    def getMediaEsami(self,voti_esami:list[int]) -> float :
        # se la lista non è vuota
        if voti_esami:
            #calcola la somma
            somma:int = 0
            for voto in voti_esami:
                somma+= voto
            
            return round(somma/len(voti_esami),2)
        # se la lista è vuota
        else:
            return 0.00
        
    # metodo che consente di confrontare oggetti della classe studente e stabelire se questi oggetti sono uguali o meno
    def __eq__(self, other) -> bool:
        # se other è non oppure se other non è un istanza della classe studente reitorno False
        if other is None or not isinstance(other,type(self)):
            return False
        
        # altrimenti valuta la seguente ugualianza
        else:
            return self.getMatricola() == other.getMatricola()


    '''
   attributi ereditati della classe Persona
   self.name
   self.last_name
   self.age
   attributi classe studente
   self.matricola
    def inheritanceTest(self):
        # verificare che la classe studenti erediti gli attributi della classe persona
        self.name
        self.last_name
        self.age

        # verificare che la classe studente erediti tutti i metodi della classe Persona
        self.getName()
        self.getLast_name()
        self.getAge() 
    '''