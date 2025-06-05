#4 - O Secretário de Segurança Pública do Rio de Janeiro, entrou em contato com você de forma urgente e te solicitou um auxílio, para obter algumas informações que serão apresentadas ao Governador do Estado:
import pandas as pd
ocorrencias = [ 
['Rio de Janeiro',6775561,35000], 
['Niteroi',515317,2500], 
['São Gonçalo',1091737,15000], 
['Duque de Caxias',924624,12000], 
['Nova Iguaçu',821128,10000], 
['Belford Roxo',513118,9000], 
['São João de Meriti',471906,8500], 
['Petrópolis',306678,1000], 
['Volta Redonda',273988,2000], 
['Campos dos Goytacazes',507548,4000], 
]
colunas=["Cidade", "População", "Roubo de pedestres"]
df_ocorrencias=pd.DataFrame(ocorrencias, columns=colunas)
#- O total e a média de roubos a pedestres no Estado do Rio de Janeiro no último semestre.
soma_roubos=df_ocorrencias["Roubo de pedestres"].sum()
media_roubos=df_ocorrencias["Roubo de pedestres"].mean()
print(soma_roubos)
print(media_roubos)
#- O total e a média da população no Estado do Rio de Janeiro.
soma_populacao=df_ocorrencias["População"].sum()
media_populacao=df_ocorrencias["População"].mean()
print(soma_populacao)
print(media_populacao)
#- O maior e o menor valor encontrado em relação aos roubos de pedestres.
maior_roubos=df_ocorrencias["Roubo de pedestres"].max()
menor_roubos=df_ocorrencias["Roubo de pedestres"].min()
print(maior_roubos)
print(menor_roubos)
#- O maior e o menor valor encontrado em relação a população.
maior_populacao=df_ocorrencias["População"].max()
menor_populacao=df_ocorrencias["População"].min()
print(maior_populacao)
print(menor_populacao)
#- O nome do município com maior e menor índice de roubos a pedestres.
maior_roubos_cidade=df_ocorrencias[df_ocorrencias["Roubo de pedestres"] == maior_roubos]["Cidade"]
menor_roubos_cidade=df_ocorrencias[df_ocorrencias["Roubo de pedestres"] == menor_roubos]["Cidade"]
print(maior_roubos_cidade)
print(menor_roubos_cidade)
#- O nome do município com maior e menor quantidade de pessoas.
maior_populacao_cidade=df_ocorrencias[df_ocorrencias["População"] == maior_populacao]["Cidade"]
menor_populacao_cidade=df_ocorrencias[df_ocorrencias["População"] == menor_populacao]["Cidade"]
print(maior_populacao_cidade)
print(menor_populacao_cidade)
#- A taxa de roubos a pedestres por município, sabendo que para se chegar a esse número, deve-se dividir a quantidade de roubos pela quantidade da população.
def formatar(valor):
    return "{:.2f}%".format(valor)
tx_roubo = ((df_ocorrencias['Roubo de pedestres'] / df_ocorrencias['População']) * 100).apply(formatar)
print("\n---- Taxa de Roubos ----")
print(df_ocorrencias['Cidade'] + "  " + tx_roubo)


