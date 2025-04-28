def even_odd_pattern(numbers:list[int]) -> int:
    pari = []
    for x in numbers:
        if x % 2 ==0:
            pari.append(x)
    
    dispari = []
    for x in numbers:
        if x % 2 !=0:
            dispari.append(x)
    
    return pari + dispari

result = even_odd_pattern([3, 6, 1, 8, 4, 7])
print(result)

