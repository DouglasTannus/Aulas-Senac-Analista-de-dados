#3- Crie um programa que calcule a idade de uma pessoa a partir do ano de nascimento dela.

# Importar biblioteca de data e hora
import datetime

# Entrada de dados
anonascimento = int(input('Informe o ano de nascimento: '))
dataatual = datetime.date.today()
anoatual = dataatual.year

# Processamento
idade = anoatual - anonascimento

# Saída
print('A idade é:',idade)











