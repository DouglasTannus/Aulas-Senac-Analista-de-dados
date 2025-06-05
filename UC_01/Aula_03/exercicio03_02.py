# 1- Faça um programa que pergunte a uma pessoa, a sua idade, o seu peso e quanto dormiu nas últimas 24 h e diga se ela pode doar ou não sangue de acordo com as seguintes condições:• Ter entre 16 e 69 anos. • Pesar mais de 50 kg. • Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas)

idade = int(input('Informe qual a sua idade: '))
peso = int(input('Informe quanto vc pesa: '))
sono = int(input('Informe quantas horas vc dormir nas últimas 24 horas: '))

if idade > 16 and idade < 69 and peso > 50 and sono >= 6:
    print('Você pode ser doador!')
else:
    print('Infelizmente você não pode ser doador.')
if idade < 16 or idade > 69:
    print('Sua idade é incompatível!')
elif peso < 50:
    print('Seu peso é incompatível!')
elif sono < 6:
    print('Você dormiu pouco nas últimas 24 horas!')
else:
    print('Parabéns!')
    









