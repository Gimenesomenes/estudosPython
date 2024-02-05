import pandas as pd


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
