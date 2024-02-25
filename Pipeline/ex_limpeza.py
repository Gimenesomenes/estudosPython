import pandas as pd

# Exemplo de limpeza de dados
# Criando um DataFrame


data = {'Produtos': ['A', 'B', 'C', 'D', 'E'],
        'Preco': [100.0, 120.0, None, 150.0, 5000.00]}

df = pd.DataFrame(data)

print("DataFrame Original: ")
print(df)

# limpeza dos dados, tratando valores nulos e outliers na coluna preço
# substituindo os valores nulos pela média e removendo outliers

df['Preco'].fillna(df['Preco'].mean(), inplace=True)
df = df[df['Preco'] < 1000]


# DataFrame após a limpeza
print("\n DataFrame tratado: ")
print(df)