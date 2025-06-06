import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'BASES\Base_dados_sorvete_clima.csv'

# Criando o DataFrame
df_sorvete = pd.read_csv(endereco_dados,sep=',',encoding='utf-8')

# Criando o DataFrame Prdução de Sorvete
df_producao_sorvete = df_sorvete[['Data','Producao_Sorvete']]
df_producao_sorvete = df_producao_sorvete.groupby(['Data']).sum(['Producao_Sorvete']).reset_index()
print(df_producao_sorvete)

# Criando o DataFrame Temperatura Media
df_temperatura_media = df_sorvete[['Data','Temperatura_Media']]

print(df_temperatura_media)

# Criando o Array da Produção de Sorvete
array_producao_sorvete = np.array(df_producao_sorvete["Producao_Sorvete"])

# Criando o Array da Temperatura Média
array_temperatura_media = np.array(df_temperatura_media["Temperatura_Media"])

# IQR (Intervalo interquartil)
# Obtendo os Quartis da Produção de Sorvete - Método weibull
q1_producao_sorvete = np.quantile(array_producao_sorvete, 0.25, method='weibull')
q2_producao_sorvete = np.quantile(array_producao_sorvete, 0.50, method='weibull')
q3_producao_sorvete = np.quantile(array_producao_sorvete, 0.75, method='weibull')
iqr_producao_sorvete = q3_producao_sorvete - q1_producao_sorvete

# Obtendo os Quartis da Temperatura Média - Método weibull
q1_temperatura_media = np.quantile(array_temperatura_media, 0.25, method='weibull')
q2_temperatura_media = np.quantile(array_temperatura_media, 0.50, method='weibull')
q3_temperatura_media = np.quantile(array_temperatura_media, 0.75, method='weibull')
iqr_temperatura_media = q3_temperatura_media - q1_temperatura_media

# Identificando os outliers superiores e inferiores da Produção de Sorvete
limite_superior_producao_sorvete = q3_producao_sorvete + (1.5 * iqr_producao_sorvete)
limite_inferior_producao_sorvete = q1_producao_sorvete - (1.5 * iqr_producao_sorvete)

# Identificando os outliers superiores e inferiores da Temperatura Média
limite_superior_temperatura_media = q3_temperatura_media + (1.5 * iqr_temperatura_media)
limite_inferior_temperatura_media = q1_temperatura_media - (1.5 * iqr_temperatura_media)

# Filtrando o DataFrame Roubos de Veiculos
df_producao_sorvete_outliers_superiores = df_producao_sorvete[df_producao_sorvete['roubo_veiculo'] > limite_superior_producao_sorvete]
df_producao_sorvete_outliers_inferiores = df_producao_sorvete[df_producao_sorvete['roubo_veiculo'] < limite_inferior_producao_sorvete]

# Filtrando o DataFrame Furtos de Veiculos
df_temperatura_media_outliers_superiores = df_temperatura_media[df_temperatura_media['furto_veiculos'] > limite_superior_temperatura_media]
df_temperatura_media_outliers_inferiores = df_temperatura_media[df_temperatura_media['furto_veiculos'] < limite_inferior_temperatura_media]

# Verificando a existência de Outliers Inferiores para Produção de Sorvete
print('\n- Verificando a existência de outliers inferiores - Roubo de Veículos')
if len(df_roubo_veiculo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_roubo_veiculo_outliers_inferiores)

# Verificando a existência de Outliers Inferiores para Temperatura Média
print('\n- Verificando a existência de outliers inferiores - Furtos de Veículos')
if len(df_furto_veiculo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_furto_veiculo_outliers_inferiores)





























