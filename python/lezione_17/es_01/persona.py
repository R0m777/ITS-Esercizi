class Persona:
    __first_name: str
    __last_name: str
    __age: int


    def __init__(self, first_name: str, last_name: str):
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            self.__first_name = None
            print(f"Il nome inserito '{first_name}' non è una stringa!")

        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            self.__last_name = None
            print(f"Il cognome inserito '{last_name}' non è una stringa!")

        if self.__first_name is not None and self.__last_name is not None:
            self.__age = 0
        else:
            self.__age = None

    def setName(self, first_name: str) -> None:
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            print(f"Il nome inserito '{first_name}' non è una stringa!")

    def setLastname(self, last_name: str) -> None:
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            print(f"Il cognome inserito '{last_name}' non è una stringa!")

    def setAge(self, age: int) -> None:
        if isinstance(age, int):
            self.__age = age
        else:
            print("L'età deve essere un numero intero!")

    def getName(self) -> str:
        return self.__first_name

    def getLastname(self) -> str:
        return self.__last_name

    def getAge(self) -> int:
        return self.__age

    def greet(self) -> str:
        return f"Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.__age} anni!"

