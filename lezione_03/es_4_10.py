'''Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.'''

lista1 = [n for n in range(1,11)]
lista_metà = len(lista1) // 2
print(f"i primi 3 elementi sulla lista sono: {lista1[:3]}")
print(f"i 3 elementi in mezzo alla lista sono: {lista_metà}")
print(f"i 3 ultimi elementi della lista sono: {lista1[-3:]}")
