'''Start with your class from Exercise 9-1. 
Create three different instances from the class, and call describe_restaurant() for each instance.'''

class Restaurant:
    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self)->None:
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")


# Create three instances of Restaurant
restaurant1 = Restaurant("Carbonara", "Italian")
restaurant2 = Restaurant("Sushi", "Japanese")
restaurant3 = Restaurant("Tacos", "Mexican")

# Call describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
       
    
