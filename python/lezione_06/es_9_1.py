'''Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of information, 
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
 Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.'''


class Restaurant:
    def __init__(self, restaurant_name:str, restaurant_type:str, restaurant_statue:str):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.restaurant_statue = restaurant_statue

    
    def describe_restaurant(self):
            print(f"il nome del ristorante è: {self.restaurant_name}\ndi tipo {self.restaurant_type}")
    def open_restaurant(self):
            print(f"il ristorante è: {self.restaurant_statue}")
if __name__ == "__main__":
   nome = Restaurant("Pappay","Cinese","aperto")
   nome.describe_restaurant()
   statue = Restaurant("papay", "cinese", "Aperto")
   statue.open_restaurant()






    
    
        