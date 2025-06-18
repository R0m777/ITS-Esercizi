import re

def is_DNA(p) -> bool:
    return bool(re.fullmatch(r'[ACGT]+', p))

def dna(s1:str, s2:str) -> str:
    start = min(len(s1), len(s2))
    for i in range(start,0 ,-1):
        if s1.endswith(s2[:i]):
            return i
    
    return 0

'''n1 = dna(s1="CAGCTGATCGATGCTAGCCTG", s2="AGCCTGTTGCACCTAGA")
print(n1)'''

'''n2 = dna(s1="TTGACCAGGTCA", s2="AACCGGTTAA")
print(n2)'''

n3 = dna(s1="GGTACCGTGA", s2="CGTGAACCTT")
print(n3)