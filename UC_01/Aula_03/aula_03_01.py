
idade = int(input('Informe a idade: '))

if idade < 18:
    print('Você é menor de idade!')
elif idade == 18:
    print('Você tem exatos 18 anos. Acesso liberado!')
elif idade > 18 and idade <65:
    print('Acesso liberado!')
else:
    print('Acesso liberado com cautela!')

#-------------------------------------------------------------

altura = float(input('Informe a sua altura em metros: '))
sexo = input('Informe se o sexo da pessoa é M ou F: ')

m = (72.7*altura) - 58
f = (62.1*altura) - 44.7

if sexo == 'M' or sexo == 'm':
    print(f'O peso ideal para homens é {m:.0f} Kg.')
elif sexo == 'F' or sexo == 'f':
    print(f'O peso ideal para mulheres é {f:.0f} Kg.')
else:
    print('Verifique o sexo informado!')














