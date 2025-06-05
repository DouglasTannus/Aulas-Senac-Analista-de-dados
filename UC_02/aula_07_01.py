import pandas as pd
import numpy as np

# Importando a base de dados de ocorrências
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame de ocorrências
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_hom_doloso = df_ocorrencias[['ano','hom_doloso']]
df_hom_doloso = df_hom_doloso.groupby(['ano']).sum(['hom_doloso']).reset_index()
df_hom_doloso = df_hom_doloso.drop(22) # Removendo o ano de 2025 com drop
df_hom_doloso = df_hom_doloso[df_hom_doloso['ano'].between(2003,2024)] # Outro metodo para remover o ano de 2025 com between

# Exibindo a base de dados de ocorrências
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_hom_doloso)

# Obtendo o máximo das ocorrências
maximo_hom_doloso = max(df_hom_doloso['hom_doloso'])
print(f"A quantidade máxima das ocorrências de homicídio doloso foi de {maximo_hom_doloso}")

# Obtendo o mínimo das ocorrências
minimo_hom_doloso = min(df_hom_doloso['hom_doloso'])
print(f"A quantidade mínima das ocorrências de homicídio doloso foi de {minimo_hom_doloso}") 

# Obtendo a amplitude das ocorrências
amplitude_hom_doloso = max(df_hom_doloso['hom_doloso']) - min(df_hom_doloso['hom_doloso'])
print(f"A amplitude das ocorrências de homicídio doloso foi de {amplitude_hom_doloso:.0f}")

# Obtendo a mediana das ocorrências
mediana_hom_doloso = np.median(df_hom_doloso['hom_doloso'])
print(f"A mediana das ocorrências de homicídio doloso foi de {mediana_hom_doloso:.0f}")

# Obtendo a média das ocorrências
media_hom_doloso = np.mean(df_hom_doloso['hom_doloso'])
print(f"A média das ocorrências de homicídio doloso foi de {media_hom_doloso:.0f}")

# Obtendo o coeficiente de amplitude das ocorrências
coeficiente_amplitude_hom_doloso = (amplitude_hom_doloso/media_hom_doloso)*100
print(f"O coeficiente de amplitude das ocorrências de homicídio doloso foi de {coeficiente_amplitude_hom_doloso:.2f} %")

# Obtendo a distância entre a média e a mediana das ocorrências
distancia_hom_doloso = abs((media_hom_doloso - mediana_hom_doloso) / mediana_hom_doloso)*100
print(f"A distância entre a média e a mediana das ocorrências de homicídio doloso foi de {distancia_hom_doloso:.2f}%")

# Obtendo o desvio padrão das ocorrências
desvio_hom_doloso = np.std(df_hom_doloso['hom_doloso'])
print(f"O desvio padrão das ocorrências de homicídio doloso foi de {desvio_hom_doloso:.0f}")




