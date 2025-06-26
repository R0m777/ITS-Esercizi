import random

def genera(dim:int) -> list[list[int]]:
    matrice:list[list[int]] = []
    
    for r in range(dim):
        row:list[int] = []

        for c in range(dim):
            while True:
                x = random.randint(0,13)

                if c == 0:
                    row.append(x)
                    break
                if x != row[0]:
                    row.append(x)
                    break

        matrice.append(row)

    return matrice

mat = genera(5)
for r in mat:
    print(r)



