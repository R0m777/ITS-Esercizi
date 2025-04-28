''' Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides, 
and it should print a summary of the sandwich that’s being ordered. 
Call the function three times, using a different number of arguments each time.'''

def sandwich(*args:tuple) -> tuple:
    return args
    
ingredienti = sandwich("mozzarella", "pane", "pomodori","melanzane")
ingredienti1 = sandwich("patate", "mortadella", "kebab")
ingredienti2 = sandwich("Ciao", 2, "Hello", 8.44)
print(f"Panino 1: {ingredienti}")
print(f"Panino 2: {ingredienti1}")

if __name__ == "__main__":
    print(f"{ingredienti2}")

