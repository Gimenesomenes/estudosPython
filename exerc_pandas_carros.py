import pandas as pd     

df = pd.read_csv('carros.csv')

# print seu head com 10 linhas:

head = df.head(10) 
print(head)

#print colunas e index do dataframe

colunas_df = df.columns
print(colunas_df)

index_df = df.index
print(index_df)

# Faça um sort decrescente pelo estado com maior qtade de carros

max_carros = df.sort_values('Quant Carros', ascending=False)
print(max_carros)

# Descubra qual a proporção de carro para a população de cada estado e insira em uma nova coluna. 

proporcao = df['Quant Carros']/df['População do Estado']

#print(proporcao)

df['Carros por Habitantes'] = proporcao

# Faça um dataframe com Estado e proporção de carro por habitantes

estado_hab = df[['Estado','Carros por Habitantes']]
print(estado_hab)


