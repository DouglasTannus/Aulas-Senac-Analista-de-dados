# 1- Faça um programa que obtenha o valor para a variável HT (horas trabalhadas no mês), obtenha o valor para a variável VH (valor hora trabalhada), obtenha o valor para a variável PD (percentual de desconto) e calcule o salário bruto => SB = HT * VH, mais o total de desconto => TD = (PD/100)*SB e o salário líquido => SL = SB – TD.
# Apresentando ao final o Salário Liquido.

ht = float(input('Informe o total de horas trabalhadas no mês: '))
vh = float(input('Informe o valor da hora trabalhada: '))
pd = float(input('Informe o percentual de desconto: '))
salariobruto = ht*vh
totaldesconto = (pd/100)*salariobruto
salarioliquido = salariobruto-totaldesconto

print(f'O salário líquido é de {salarioliquido:,.2f} reais')











