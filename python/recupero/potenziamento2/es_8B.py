def mcd(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return x if x > 1 else 1

n1 = mcd(x=18, y=12)
print(n1)
