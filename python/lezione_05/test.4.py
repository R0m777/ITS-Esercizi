def somma_elementi(x:list[int], y:list[int])-> int:
    risultato:list = []
    for i in range(len(x)):
        risultato.append(x[i] + y[i])
    return risultato


print(somma_elementi([1, 1, 1], [1, 1, 1]))

