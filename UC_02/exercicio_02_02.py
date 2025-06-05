#2- Escreva um programa que leia uma série com 10 idades e ao final separe as que estão iguais e acima de 18 anos das que estão abaixo de 18 anos.

import pandas as pd

idades = pd.Series([15,16,17,18,19,20,21,22,23,24])
demaior = idades[idades>=18]
demenor = idades[idades<18]
print(demaior.to_string(index=False)) #(to_string...) remover coluna de índice
print(demenor)














