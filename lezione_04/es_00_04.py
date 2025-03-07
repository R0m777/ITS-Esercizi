'''Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5, and “equal” if it’s equal to 5'''

def check_each(a:int, b:int, c:int):
    return[a,b,c]
a = int(input("inserisci un numero intero: "))
b = int(input("inserisci un altro numero intero: "))
c = int(input("inserisci un 3 numero: "))
numbers = check_each(a,b,c)
for i in numbers:
    if i > 5:
        print(f"{i} is bigger than 5.")
    elif i < 5:
        print(f"{i} is smaller than 5.")
    else:
        print(f"{i} is equal to 5.")