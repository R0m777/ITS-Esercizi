class Persona:
    def __init__(self):
        self.name:str = ""
        self.last_name:str = ""
        self.age:int = 0

    # funzione che mi mostri in output i dati relativi ad una persona
    def displayData(self)-> None:
        print(f"Nome: {self.name}\nCognome: {self.last_name}\nEtà: {self.age}")
    
    # funzione che mi consenta di impostare il valore di self.name
    def setName(self, name:str) -> None:
        self.name = name 

    # funzione che mi consenta di impostare il valore self.last_name
    def setLast_name(self,last_name:str) -> None:
        self.last_name = last_name

    # finzione che mi consenta di impostare il valore di self.age
    def setAge(self, age:int) -> None:
        if age < 0 or age > 120:
            self.age = 0
        else:
            self.age = age

    # funzione che mi consenta di ritornare il valore di self.name
    def getName(self) -> str:
        return self.name
    
    # funzione che mi consenta di ritornare il valore di self.last_name
    def getLast_name(self) -> str:
        return self.last_name
    
    #funzione che mi consenta di ritornare il valore di self.age
    def getAge(self) -> int:
        return self.age
