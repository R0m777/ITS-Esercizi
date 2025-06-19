def proDict() -> dict:
    risultato:dict = {}
    for x in range(101):
        for y in range(2,90,2):
            risultato[(x,y)] = x * y
    
    return risultato

d = proDict()

print(d[(13,88)])