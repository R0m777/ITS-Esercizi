import time

def sort(lista):
   
    n = len(lista)
    for i in range(n):
      
      swapped = False

      for j in range(n-1):
         if lista[j] > lista[j + 1]:

            lista[j], lista[j + 1] = lista[j +1], lista[j]

            swapped = True

      if not swapped:
         break
    
    return lista      


lista = [2,5,4]
print(sort(lista=lista))
lista2 = [45,66,765,44,895]
print(sort(lista=lista2))