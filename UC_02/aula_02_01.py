#Script utiliando Series

import pandas as pd
notas = pd.Series([7, 8, 6, 9, 2, 1, 3, 5, 4, 10])
notas_altas = notas[notas>=7]
notas_baixas = notas[notas<7]
print('\n-- Notas maiores ou iguais a 7 --')
print(notas_altas)
print('\n-- Notas menores que 7 --')
print(notas_baixas)
