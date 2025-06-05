 
# Importando a Biblioteca
import pandas as pd
import numpy as np

# Importando a Base de Dados
endereco_dados = 'BASES\Funcionarios.csv'

# Criando o DataFrame Funcionários
df_funcionarios = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

# Criando um array para o salário
array_salario = np.array(df_funcionarios['Salário'])

# Criando um array para a idade
array_idade = np.array(df_funcionarios['Idade'])

# Criando um array para o tempo de empresa
array_tempo = np.array(df_funcionarios['Tempo'])

# Obtendo as métricas solicitadas
media_salario = np.mean(array_salario)
mediana_salario = np.median(array_salario)
distancia_salario = abs((media_salario - mediana_salario)/mediana_salario)*100
maior_salario = np.max(array_salario)
menor_salario = np.min(array_salario)
amplitude_salario = maior_salario - menor_salario
nome_salario = df_funcionarios[df_funcionarios['Salário'] == maior_salario]['Nome']

media_idade = np.mean(array_idade)
mediana_idade = np.median(array_idade)
distancia_idade = abs((media_idade - mediana_idade) / mediana_idade)*100
maior_idade = np.max(array_idade)
menor_idade = np.min(array_idade)
amplitude_idade = maior_idade - menor_idade
nome_velho = df_funcionarios[df_funcionarios['Idade'] == maior_idade]['Nome']
nome_novo = df_funcionarios[df_funcionarios['Idade'] == menor_idade]['Nome']

media_tempo = np.mean(array_tempo)
mediana_tempo = np.median(array_tempo)
distancia_tempo = abs((media_tempo - mediana_tempo)/mediana_tempo)*100
maior_tempo = np.max(array_tempo)
menor_tempo = np.min(array_tempo)
amplitude_tempo = maior_tempo - menor_tempo
nome_tempo = df_funcionarios[df_funcionarios['Tempo'] == maior_tempo]['Nome']

qtd_func = np.count_nonzero(array_idade)

# Exibindo as Métricas
print('\n----------- Tabela de Funcionários -------------')
print(df_funcionarios)
print('\n-------- Exibindo os Resultados Solicitados --------')

print(f'O Funcionário com maior salário na empresa possui {maior_salario} reais.')
print(f'O Funcionário com menor salário na empresa possui {menor_salario} reais.')
print(f'A média salarial dos funcionários é {media_salario:.0f}')
print(f'A mediana do salário dos funcionários é {mediana_salario:.0f} reais.')
print(f'A distância entre a média e a mediana do salário dos funcionários é {distancia_salario:.1f}% anos')
print(f'A Amplitude relativa aos salários de empresa é {amplitude_salario} reais.')
print(f'{nome_salario.values[0]} é o funcionário com maior salário.')

print(f'\n{nome_velho.values[0]} é o funcionário com mais idade da empresa, com {maior_idade} anos')
print(f'{nome_novo.values[0]} é o funcionário com menos idade da empresa, com {menor_idade} anos')
print(f'A Amplitude relativa a idade dos funcionários da empresa é {amplitude_idade} anos')
print(f'A média da idade dos funcionários é {media_idade:.0f} anos')
print(f'A mediana da idade dos funcionários é {mediana_idade:.0f} anos')
print(f'A distância entre a média e a mediana da idade dos funcionários é {distancia_idade:.1f}% anos')

print(f'\n{nome_tempo.values[0]} é o funcionário com mais tempo de empresa') 
print(f'O Funcionário com maior tempo de empresa possui {maior_tempo} anos')
print(f'O Funcionário com menor tempo de empresa possui {menor_tempo} anos')
print(f'A Amplitude relativa ao tempo de empresa é {amplitude_tempo} anos')#Amplitude está muito próxima do maior valor, dados discrepantes
print(f'O tempo médio dos funcionários na empresa é {media_tempo:.0f} anos')
print(f'A distância entre a média e a mediana do tempo de empresa dos funcionários é {distancia_tempo:.1f}% anos')

print(f'\nA quantidade de funcionários na empresa são {qtd_func}')