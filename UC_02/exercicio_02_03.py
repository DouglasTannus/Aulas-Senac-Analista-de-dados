#3- O Delegado responsável pela Delegacia de roubos e furtos de automóveis, entrou em contato com você e te solicitou um auxílio, para obter duas informações:
#- A quantidade de roubos de automóveis + furto de automóveis diária, dos últimos 7 dias.
#- A taxa de recuperação de automóveis diária, dos últimos 7 dias, sabendo que para se chegar a esse número, deve-se dividir a quantidade de recuperação de automóveis pela quantidade de roubo de automóveis.
#Ele te enviou os seguintes dados:
#● Roubo de automóveis: 100,90,80,120,110,90,70
#● Furto de automóveis: 80,60,70,60,100,50,30
#● Recuperação de automóveis: 70,50,90,80,100,70,50
#E pediu para apresentar na tela o resultado das informações solicitadas.
import pandas as pd

def formatar(valor):
    return"{:.2f}%".format(valor) # pode ser qualquer variável no lugar de valor

# "index" é a primeira coluna gerada (se deixar vazio, ficam números partindo do zero)
roubos = pd.Series([100,90,80,120,110,90,70], index=['Seg','Ter','Qua','Qui','Sex','Sab','Dom'])
furtos = pd.Series([80,60,70,60,100,50,30], index=['Seg','Ter','Qua','Qui','Sex','Sab','Dom'])
recuperacoes = pd.Series([70,50,90,80,100,70,50], index=['Seg','Ter','Qua','Qui','Sex','Sab','Dom'])
ocorrencias = roubos + furtos
eficiencia = ((recuperacoes/roubos)*100).apply(formatar) # aplicar função criada
eficiencia_acumulada = (recuperacoes.sum()/(roubos.sum()+furtos.sum()))*100

print('\nRoubos de automóveis + furto de automóveis por dia:') # "\n" para pular linha
print(ocorrencias)
print('\nTaxa de recuperação de automóveis diária:')
print(eficiencia)

# Outras métricas
print(f'\nAcumulado de roubo de veículos: {roubos.sum()}')
print(f'\nAcumulado de furtos de veículos: {furtos.sum()}')
print(f'\nAcumulado de recuperação de veículos: {recuperacoes.sum()}')
print(f'\nPercentual de recuperação do acumulado de roubos e furots: {eficiencia_acumulada:.2f}%')


