import pandas as pd


dados = {
    'Nome':['Max','Bella','Rocky','Luna'],
    'Raça':['Labrador', 'Poodle','Boxer','Golden Retriever'],
    'Cor':['Amarelo', 'Branco', 'Marrom', 'Dourado'],
    'Peso (kg)':[60,35,65,55],
    'Altura (cm)':[30,7,28,25],
    'Data de Nascimento':['01/05/2018','10/12/2019','03/08/2017','12/02/2016']

}

#Criar o DataFrame

df_cachorros = pd.DataFrame(dados)
print(df_cachorros)


describe = df_cachorros.describe()

print(describe)

# Extraindo valores
valores = df_cachorros.values
print(valores)

# Extraindo colunas

colunas = df_cachorros.columns
print(colunas)

# Extraindo index

index = df_cachorros.index
print(index)

# Ordenação de coluna

ordena_cresc = df_cachorros.sort_values('Altura (cm)')
print(ordena_cresc)

# Ordenar ao contrário

ordena_descrec = df_cachorros.sort_values('Altura (cm)', ascending=False)
print(ordena_descrec)

# Ordena multiplas colunas

ordena_mul = df_cachorros.sort_values(['Altura (cm)', 'Peso (kg)'])
print(ordena_mul)

# focando apenas em uma coluna

nomes = df_cachorros['Nome']
print(nomes)

# Lógica dentro de colchetes

grandes = df_cachorros[df_cachorros['Altura (cm)'] >20]
print(grandes)


# Subconjunto com base em dados de texto 

boxer = df_cachorros[df_cachorros['Raça'] == 'Boxer']
print(boxer)

# Separar por datas
# Tem que converter para datetime

df_cachorros['Data de Nascimento'] = pd.to_datetime(df_cachorros['Data de Nascimento'], format='%d/%m/%Y')


data = df_cachorros[df_cachorros['Data de Nascimento'] <'12/05/2017']

print(data)


## Adicionando uma nova coluna

df_cachorros['Altura (m)'] = df_cachorros['Altura (cm)'] / 100

altura = df_cachorros

print(altura)

# extrair dados de um tipo de coluna

altura_max = df_cachorros['Altura (cm)'].max()

print(altura_max)

# groupby

min_max = df_cachorros.groupby('Cor')['Peso (kg)'].agg([min,max,sum])
print(min_max)