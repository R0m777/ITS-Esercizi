'''9-5.
Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3.
Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
Print login_attempts again to make sure it was reset to 0.'''

class User:
    def __init__(self, first_name:str, last_name:str, age:int, location:str, occupation:str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0  

    def describe_user(self)->None:
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Occupation: {self.occupation}")
        print(f"Login Attempts: {self.login_attempts}")

    def greet_user(self)->None:
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

    def increment_login_attempts(self)->int:
        self.login_attempts += 1

    def reset_login_attempts(self)->int:
        self.login_attempts = 0


user = User('Derek', 'Nguyen', 35, 'San Francisco', 'Data Analyst')

# Call
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()


print(f"\nLogin attempts after increments: {user.login_attempts}")


user.reset_login_attempts()

print(f"Login attempts after reset: {user.login_attempts}")
