import pandas as pd 
import numpy as np 


# A empresa Carri Construtora contratou a empresa que você trabalha para encontrar possíveis compradores para o seus novos empreendimentos.
# A empresa quer entender as necessidades dos clientes, e quer informações com:
# Quais clientes devemos abordar;
# Qual empreendimento nós devemos mostra-los;
# Esse cliente está em busca em investir em um imóvel ou comprar para moradia? 


# Iniciando abrindo o arquivo csv

df_research = pd.read_csv('research people.csv')

# visualizando DataFrame
print(df_research.head())


# Achando a coluna Unnamed e entendendo se podemos retirar ela ou não
print(df_research['Unnamed: 0'])


# Retirando a coluna Unnamed
df_research = df_research.drop(columns='Unnamed: 0')

#print(df_research)

# Nome de colunas com problemas, ex: "Endereeço". Renomear essas colunas.

#print(df_research.columns)

# Criando um dicionário para renomea-lás

novas_cols = {'Endereerço':'Endereço',
              'phone':'Telefone',
              'anual_income':'Renda Anual',
              'AAge':'Idade',
              'n_filhos':'N filhos',
              'Food_restrictions':'Restrição alimentar',
              'streaming':'Streaming',
              'diariamente_sun blocker':'Usa protetor solar diariamente',
              
              }

# Renomeando as colunas

df_research.rename(columns=novas_cols, inplace=True)
print(df_research.head())

# Alguns nomes da coluna Nome vieram com caracteres especiais.

#print(df_research['Nome'])

# Devemos limpar isso também 
# O \W equivale a [^a-zA-Zà-úÀ-Ú0-9_].

df_research.Nome = df_research.Nome.str.replace('[^a-zA-Zà-úÀ-Ú0-9 ]','')

print(df_research.head())

# Fazer tratamento da coluna telefone, que apresenta também caracteres especiais 

#print(df_research['Telefone'])

df_research.Telefone = df_research.Telefone.str.replace('[^0-9() +-]','*')
df_research.loc[df_research.Telefone.str.contains('[*]', na=False), 'Telefone'] = np.nan

print(df_research['Telefone'])

# Fazendo tratamento da coluna Estado Civil

#print(df_research['Estado Civil'])

df_research['Estado Civil'] = df_research['Estado Civil'].replace({'C':'Casado', 
                                                                   'S':'Solteiro', 
                                                                   'D':'Divorciado',
                                                                   'V':'Viúvo'
                                                                   })
print(df_research['Estado Civil'])

#print(df_research.columns)

# Fazendo a limpeza de dados que não são necessários para o negócio, como: Restrição alimentar, compra e lê livros.. qtdade de livros.. autor

# Nesse caso fazemos um drop do DataFrame para deixa-lo mais limpo

df_carri = df_research.copy()

df_drop = ['Restrição alimentar', 
           'Streaming',
            'Usa protetor solar diariamente', 
            'Compra e Lê Livros Todos os Anos', 
            'Quantidade de Livros Comprados',
            'Autor Favorito'
           ]

df_carri.drop(columns=df_drop, inplace=True)

#print(df_carri)

#print(df_carri.describe())

# Adicionando coluna

df_carri['Minha Casa Minha Vida'] = True

# Adicionando coluna investimento

df_carri['Investimento'] = np.where((df_carri.Moradia == 'Quitada') | (df_carri.Moradia == 'Financiamento'), True, False)

print(df_carri)



#print(df_carri)












