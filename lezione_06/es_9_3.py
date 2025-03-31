'''Given is the class Animal. For each task, test your changes!
1. Create two realistic instances of Animals
2. Print the name of each object
3. Change the amount of legs of one object using the dot notation
4. Add a method setLegs() to set the legs of an object and repeat task 3 but
this time using the method.
5. Add a method getLegs() to return the amount of legs
6. Add a method named printInfo that prints all attributes of the Animal'''

class Animal:
    def __init__(self):
        self.animal_name:str = ""
        self.animal_legs:int = 0

    def animal_data(self) -> None:
        print(f"Nome: {self.animal_name}\nLegs: {self.animal_legs}")

    def setName(self,animal_name) -> None:
        self.animal_name = animal_name
        

    def setLegs(self, animal_legs) -> None:
        if animal_legs > 70:
           self.animal_legs = 0
        else:
           self.animal_legs = animal_legs 

    def getLegs(self, animal_legs) -> int:
        return animal_legs
    
pd:Animal = Animal()

pd.animal_data()
print("-"*30)
pd.setName("Formica")
pd.setLegs(6)
pd.animal_data()
    
    
        
    
    
    


