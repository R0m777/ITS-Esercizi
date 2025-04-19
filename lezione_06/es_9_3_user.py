'''Make a class called User. 
Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile.
 Make a method called describe_user() that prints a summary of the user’s information. 
 Make another method called greet_user() that prints a personalized greeting to the user. 
Create several instances representing different users, and call both methods for each user.'''

class User:
    def __init__(self, first_name:str, last_name:str, age:int, location:str, occupation:str):
        if not (17<age<80):
            raise ValueError("Age must be between 18 and 79")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation

    def describe_user(self)-> None:
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self)-> None:
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

# User
user1 = User("Paperino", "Bianco", 30, "Milano", "Pagliaccio")
user2 = User("Pino", "Nero", 45, "Napoli", "Magazziniere")
user3 = User("Jennifer", "Lopez", 60, "Los Angeles", "Cantante")

# Calling methods
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

        
