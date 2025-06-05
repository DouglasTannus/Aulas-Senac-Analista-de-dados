#2- Escreva um programa que, dados 3 números inteiros (n1, n2 e n3), diga qual deles é maior.

n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
n3 = int(input('Informe o terceiro valor: '))

if n1>n2 and n1>n3:
    print(f'{n1} é o maior valor')
elif n2>n3 and n2>n1:
    print(f'{n2} é o maior valor')
elif n3>n1 and n3>n2:
    print(f'{n3} é o maior valor')
else:
    print('Existem pelo menos dois números iguais')
    









