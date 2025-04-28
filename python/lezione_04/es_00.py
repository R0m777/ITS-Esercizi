'''sum:float = 0
for x in range(1,11):
    sum+=x
    
print(f"La somma dei numeri compresi tra 1 e 10 è: {sum}")'''


'''a:float = float(input("inserisci un numero intero: "))
b:float = float(input("inserisci un altro numero intero: "))   
def suminrange(a:float, b:float):
    
    result = 0

    for i in range(a,b+1):
        result = result + i

    return result


print(f"la somma dei numeri tra {a} e {b} = {suminrange(a,b)}")'''

'''print(f"la somma dei numeri tra 1 e 10 è: {suminrange(1,10)}")
print(f"la somma dei numeri tra 20 e 37 è: {suminrange(20,37)}")
print(f"la somma dei numeri tra 35 e 49 è: {suminrange(35,49)}")'''



'''def subtraction(a,b) -> float:

    result = a - b
    return result

a = float(input("inserisci un numero intero: "))
b = float(input("inserisci un altro numero intero: ")) 
myresult = subtraction(a,b)
print(f"la sub di {a} - {b} = {subtraction(a,b)}")
print(type(subtraction(a,b)))'''

def add(*args):
    return max(args)

print(add(1,2,5,7))




