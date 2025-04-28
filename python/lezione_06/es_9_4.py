'''Start with your program from Exercise 9-1. 
Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, and then change this value and print it again. 
Add a method called set_number_served() that lets you set the number of customers that have been served. 
Call this method with a new number and print the value again.
 Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
Call this method with any number you like that could represent how many customers were served in, say, a day of business. '''

class Restaurant:
    def __init__(self, restaurant_name:str, restaurant_type:str, restaurant_statue:str, costomers:int):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.restaurant_statue = restaurant_statue
        self.costomers = costomers
        

    
    def describe_restaurant(self) -> None:
            print(f"il nome del ristorante è: {self.restaurant_name}\ndi tipo {self.restaurant_type}\nè {self.restaurant_statue}\nHa servito: {self.costomers}")
        
    def setNumber(self,costomers) -> None:
         self.costomers = costomers

    def __call__(self) -> int:
         return self.costomers
    
pd:Restaurant = Restaurant("Pizzeria","Italiano","Aperto!!", 7)
pd.describe_restaurant()

         
    
          

