# users.py

class User:
    def __init__(self, first_name:str, last_name:str, username:str, email:str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self)->None:
        print(f"\nUser Info:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def greet_user(self)->None:
        print(f"Welcome, {self.username}!")

class Privileges:
    def __init__(self, privileges:str):
        self.privileges = privileges

    def show_privileges(self)->None:
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")

class Admin:
    def __init__(self, user:str, privileges:str):
        self.user = user
        self.privileges = privileges
