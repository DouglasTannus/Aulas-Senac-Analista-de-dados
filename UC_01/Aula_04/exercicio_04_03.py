# 4- Construa um programa onde serão fornecidas as duas notas de dez alunos.                       
#Calcule a média de cada aluno e mostre a situação de cada aluno de acordo com as seguintes condições:
#- Se a média for maior igual a 70 -> ATENDIDO
#- Se a média for maior igual a 30 e menor que 70 -> PARCIALMENTE ATENDIDO
#- Se a média for menor que 30 -> NÃO ATENDIDO

for i in range(3):
    nome=input("Informe o nome do aluno: ")
    nota1 = float(input("Informe a primeiro nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    media=(nota1+nota2)/2

    if media>=7.0:
        situacao="ATENDIDO"
    elif media<7.0 and media>=3.0:
        situacao="PARCIALMENTE ATENDIDO"
    else:
        situacao="NÃO ATENDIDO"

    print(situacao)



















