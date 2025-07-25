import numpy as np
import random



# Matrice 3x3 di numeri interi casuali tra 0 e 9
matrice_randint = np.random.randint(0, 10, size=(3, 3))
print(matrice_randint)

# Array di valori da 0 a 9
array_range = np.arange(10)
print(array_range)

# Array di valori da 0 a 10 con passo 2
array_range_step = np.arange(0, 10, 2)
print(array_range_step)

# Array di 10 valori equispaziati tra 0 e 1
array_linspace = np.linspace(0, 1, 10)
print(array_linspace)