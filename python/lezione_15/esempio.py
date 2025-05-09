'''PATH: str = "lezione_15/example.txt"

file = open(PATH, "r", encoding="utf-8")
print(file.read())'''

'''file = open("lezione_15/example.txt", "a")
try:
    pass
finally:
    file.close()'''

'''with open("lezione_15/example.txt", "w") as file:
    print(file.read())'''

'''class MyResources:

    def __enter__(self):
        print("Sono nella funzione __enter__")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Sono nella funzione __exit__")

        if exc_type is not None:
            print(f"Error: {exc_value}")
        return True
    
print("Inizio programma")

with MyResources() as rescources:
    print("sono dentro il blocco with")


with open("lezione_15/example.txt") as reader:
    print(reader.read())'''

import json

file = open("lezione_15/config.json","w")

db: dict = {"gdhdhd": {"ciao":"mincia", "age": 30},
            "hjdjksahj": {"giovanni": "name"}}

json.dump(db, file)

file.close()
