'''PATH: str = "lezione_15/example.txt"

file = open(PATH, "r", encoding="utf-8")
print(file.read())'''

'''file = open("lezione_15/example.txt", "a")
try:
    pass
finally:
    file.close()'''

with open("lezione_15/example.txt", "w") as file:
    print(file.read())