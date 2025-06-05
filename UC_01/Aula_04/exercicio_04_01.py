 #Escreva um programa que, dado 5 números inteiros calcule a soma deles e identifique o maior deles.

soma=0
maior=0

for i in range(5):
    n=int(input('Informe um valor inteiro: '))
    if n > maior:
        maior=n
    soma=soma+n

print(f'A soma é {soma}')
print(f'O maior número é {maior}')


