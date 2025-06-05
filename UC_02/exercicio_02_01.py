#1- Faça um programa que leia duas séries com 10 números inteiros cada e ao final mostre a soma, a subtração, a multiplicação e a divisão entre elas.
import pandas as pd
serie1 = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
serie2 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
soma = serie1 + serie2
print(soma)
subtracao = serie1 - serie2
print(subtracao)
multiplicacao = serie1 * serie2
print(multiplicacao)
divisao = serie1 / serie2
print(divisao)




