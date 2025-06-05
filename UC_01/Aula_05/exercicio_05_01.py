# 2- Construa um programa que armazene 10 números inteiros em um vetor. Ao final informe quantos números são pares e quantos são ímpares e mostre o vetor principal na ordem inversa e depois na ordem crescente.

lista=[]
lista_pares=[]
lista_impares=[]

for i in range(10):
    lista.append(int(input("Informe um número inteiro: ")))

for i in range(10):
    if lista[i]%2==0:
        lista_pares.append(lista[i])
print(lista_pares)
print(f"Temos {len(lista_pares)} números pares")

for i in range(10):
    if lista[i]%2!=0:
        lista_impares.append(lista[i])
print(lista_impares)
print(f"Temos {len(lista_impares)} números ímpares")

lista.sort(reverse=True)
print(lista)

lista.sort()
print(lista)






