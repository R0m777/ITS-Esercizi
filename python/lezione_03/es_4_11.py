'''Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
Print the message My friend’s favorite pizzas are:, 
and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.'''

lista_pizza = ["Margerita", "Marinara", "Caprese"]
friend_pizzas = []
friend_pizzas.extend(lista_pizza)
lista_pizza.append("Quatro formaggi")
friend_pizzas.append("Diavola")

for pizza in lista_pizza:
    print(f"my favorit pizzas are: {lista_pizza}")
    break 
    

for pizza in friend_pizzas:
    print(f"My friend favorit pizzas are: {lista_pizza}")
    break
    