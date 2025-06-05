'''Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 45'''

x = [x for x in range(2,15,2)]
print(x)

y = [y for y in range(1,14,3)]
print(y)

z = [z for z in range(0,31,5)]
z.reverse()
print(z)

i = [i for i in range(5,46,10)]
print(i)