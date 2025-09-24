from abc import ABC, abstractmethod
class Forma(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def getArea(self):
        pass

    def render(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato):
        super().__init__("Quadrato")
        self.lato = lato

    def getArea(self):
        return self.lato ** 2
    
    def render(self):
        pass

class Triangolo(Forma):
    def __init__(self, lato):
        super().__init__("Triangolo")
        self.lato = lato

    def getArea(self):
        return (self.lato * self.lato) / 2
    
    def render(self):
        pass

