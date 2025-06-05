# 1- Utilizando apenas o conceito de repetição, faça um programa para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um novo valor, pois o segundo valor não pode ser igual a zero. Ao final imprimir o resultado da divisão do primeiro valor pelo segundo valor.

for i in range(3):
    valor1 = float(input('Informe o primeiro valor: '))
    valor2 = float(input('Informe o segundo valor: '))

    if valor2 == 0:
        valor2= float(input("Informe um novo valor, diferente de zero: "))
                      
    divisao = valor1/valor2

    print(divisao)


    













