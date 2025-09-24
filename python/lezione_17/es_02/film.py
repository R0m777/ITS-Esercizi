class Film:

    __id : int
    __titolo: str

    def __init__(self, id:int, titolo:str):
        self.__id = id
        self.__titolo = titolo

    def setID(self, id:int):
        self.__id = id

    def setTitle(self, titolo:str):
        self.__titolo = titolo

    def getID(self):
        return self.__id
    
    def getTitle(self):
        return self.__titolo
    
    def isEqual(self, otherFilm:int) -> bool:
        return self.__id == otherFilm 
           