'''Given is the class Animal. For each task, test your changes!
1. Create two realistic instances of Animals
2. Print the name of each object
3. Change the amount of legs of one object using the dot notation
4. Add a method setLegs() to set the legs of an object and repeat task 3 but
this time using the method.
5. Add a method getLegs() to return the amount of legs
6. Add a method named printInfo that prints all attributes of the Animal'''

class Animal:
    def __init__(self,animal_name:str, animal_legs:int):
        self.animal_name = animal_name
        self.animal_legs = animal_legs

    def animal_data(self):
        print(f"Nome: {self.animal_name}\nLegs: {self.animal_legs}")
        
    
    
    


