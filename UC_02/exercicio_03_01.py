# 1 – O Ministro da Saúde, entrou em contato com você e te solicitou um auxílio, para obter as seguintes informações sobre os dados da vacinação da covid nos últimos quatro anos:
#- O total e a média de pessoas vacinadas no período.
#- O total e a média da população do Brasil.
#- A taxa de vacinação anual, dos últimos 4 anos, sabendo que para se chegar a esse número, deve-se dividir a quantidade de vacinados pela quantidade da população.
#Ele te enviou os seguintes dados:
#● População Vacinada: 30000000, 25000000, 10000000, 5000000
#● População Total: 213317639, 214477744, 215574303, 216687971
#E pediu para apresentar na tela o resultado das informações solicitadas.
import pandas as pd

def formatar(valor):
    return "{:.2f}%".format(valor)

def formatar_milhar(milhar):
    return '{:,.0f}'.format(milhar)

vacinados = pd.Series([30000000, 25000000, 10000000, 5000000],index = ['2021', '2022', '2023', '2024'])
pop_total = pd.Series([213317639, 214477744, 215574303, 216687971], index = ['2021', '2022', '2023', '2024'])
tot_vac = (vacinados.sum())
med_vac = (vacinados.mean())
tot_pop = (pop_total.sum())
med_pop = (pop_total.mean())
tx_vac_anual = ((vacinados/pop_total)*100).apply(formatar)

print(f'\nO total de vacinados nos últimos quatro anos é: \n{tot_vac}')
print(f'\nA média de vacinados nos últimos quatro anos é: \n{med_vac}')
print(f'\nO acumulado da população total nos últimos quatro anos é: \n{tot_pop}')
print(f'\nA média da população nos últimos quatro anos é: \n{med_pop}')
print(f'\nA taxa anual de vacinação nos últimos quatro anos é: \n{tx_vac_anual}')



print(f'O valor mais recente é: {pop_total.tail(1).iloc[0]}') 
#tail - trazer um valor da série, neste caso, o último
#iloc - remover coluna de índices










