#2- Escreva um programa que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula: valorfinal = prestacao+(prestacao*(taxa/100)*tempo)

#Entrada dos dados
prestacao = float(input('Informe o valor da prestação: '))
taxa = float(input('Informe a taxa em valor percentual: '))
tempo = int(input('Informe o tempo de atraso em dias: '))

#Processamento dos dados
juros = prestacao*(taxa/100)*tempo
valorfinal = prestacao+juros

#Saída de dados
print(f'O pagamento se encontra atrasado em {tempo} dias, os juros da prestação são de R${juros:,.2f}, portanto o valor final a ser pago será de: R${valorfinal:,.2f}')









