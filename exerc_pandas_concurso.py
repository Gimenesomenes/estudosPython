import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# Quantas pessoas são do estado do piaui? 

df_concurso = pd.read_csv('dados_concurso.csv')

# exibir o head 

head = df_concurso.head()
print(head)

estado = df_concurso[df_concurso['Estado'] == 'PI'].count()

print(estado)

# utilizando groupby para pegar agrupar por estado

group_estado = df_concurso[['Número de Inscrição', 'Estado']].groupby('Estado').count()
print(group_estado)

# Qual a distribuição de escolaridade por estado?

escolaridade = df_concurso[['Estado', 'Escolaridade','Número de Inscrição']].groupby(['Estado','Escolaridade']).count()
print(escolaridade)


# Qual é a porcentagem de pessoas com deficiência? 

pcd = df_concurso['Deficiência'].value_counts(normalize=True) * 100
print(pcd)

# Retorne o dado com número de inscrição, nome e data de nascimento.

colunas_concurso = df_concurso.columns
print(colunas_concurso)
dados_concurso = df_concurso[['Número de Inscrição', 'Data de Nascimento','Nome']]
print(dados_concurso)

# Quantas pessoas nasceram antes de 1995? 
df_concurso['Data de Nascimento'] = pd.to_datetime(df_concurso['Data de Nascimento'])
print(df_concurso['Data de Nascimento'])


data = df_concurso['Data de Nascimento'].loc[df_concurso['Data de Nascimento'] > np.datetime64('1995')].count()

print(data)

antes_ano_95 = df_concurso.loc[df_concurso['Data de Nascimento'] < np.datetime64('1995')]
print(antes_ano_95)

# Quais foram os 10 primeiros inscritos? 

data_inscrição = df_concurso.set_index('Data de Inscrição').sort_index()[:10]
print(data_inscrição)

# Retorna bool em relação a valores faltosos
falta_dados = df_concurso.isna().any()
print(falta_dados)

# Retona qtos valores faltosos tem na coluna

falta_dados_sum = df_concurso.isna().sum()
print(falta_dados_sum)

df_concurso.isna().sum().plot(kind='bar')
plt.show()

# Recomendo dados nulos

remove_nan = df_concurso.dropna()
print(remove_nan)

# Substituindo valores nulos 

substitui_nan = df_concurso.fillna("Falta informação.")
print(substitui_nan)


