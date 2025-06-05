# 3- Faça um programa que verifique a quantidade de acertos de uma prova com cinco questões, sabendo que serão fornecidos pelo usuário as letras assinaladas em cada questão. Para isso será criado um vetor chamado GABARITO com as seguintes respostas: A, B, B, D, E.

gabarito=['A','B','B','D','E']
prova=[]
acerto=0
erro=0
n=1

for i in range(5):
    prova.append(input(f'Informe a letra assinalada na {n}a. questão: ').upper())
    n+=1

for i in range(len(prova)):
    if prova[i]==gabarito[i]:
        acerto+=1
    else:
        erro+=1

print(f'As alternativas assinaladas foram: \n{prova}')
print(f'O gabarito é: \n{gabarito}')
print(f'Você acertou {acerto} questões.')










