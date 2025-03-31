'''Make a class called User. 
Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile.
 Make a method called describe_user() that prints a summary of the user’s information. 
 Make another method called greet_user() that prints a personalized greeting to the user. 
Create several instances representing different users, and call both methods for each user.'''

class User:
    def __init__(self):
        self.name:str = ""
        self.last_name:str = ""

    def describeUser(self) -> None:
        print(f"User name: {self.name}\nLast name: {self.last_name}")

    def setUserInfo(self,name,last_name) -> None:
        self.name = name
        self.last_name = last_name

    def __call__(self) -> str:
        return f"User name: {self.name}\nLast name: {self.last_name}"
    

    

pd:User = User()
pd.setUserInfo("Philip", "Daoud")
pd.describeUser()
print("-"*30)
user2:User = User()
user2.setUserInfo("Marco", "Gasp")
user2.describeUser()

        
