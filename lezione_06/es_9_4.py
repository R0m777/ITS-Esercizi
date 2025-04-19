'''Start with your program from Exercise 9-1. 
Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, and then change this value and print it again. 
Add a method called set_number_served() that lets you set the number of customers that have been served. 
Call this method with a new number and print the value again.
 Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
Call this method with any number you like that could represent how many customers were served in, say, a day of business. '''

class Restaurant:
    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def describe_restaurant(self)->None:
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self)->None:
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number)->int:
        self.number_served = number

    def increment_number_served(self, increment)->int:
        self.number_served += increment


restaurant = Restaurant("Pappay", "Italian")


print(f"Number served: {restaurant.number_served}")


restaurant.number_served = 25
print(f"Number served after update: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Number served after set_number_served: {restaurant.number_served}")


restaurant.increment_number_served(30)
print(f"Number served after increment_number_served: {restaurant.number_served}")
         
    
          

