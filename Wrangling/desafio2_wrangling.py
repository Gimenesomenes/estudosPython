import pandas as pd 
import numpy as np 

# Uma empresa chamada Hillo, é uma empresa que está estudando o mercado e quer encontrar uma parceria com uma empresa de 
# Streaming (Netflix, Disney plus, etc), mas gosta de saber quais as empresas dariam retorno de investimento. eles podem fazer 
# análise de machine learning também com esses dados. 

df = pd.read_csv('research people.csv')

print(df.columns)


df_hillo = df.drop(columns='Unnamed: 0')

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

df_hillo.rename(columns=novas_cols, inplace=True)
print(df_hillo.columns)

# Excluindo dados que não são interessantes para o nosso negócio.

df_hillo = df_hillo.drop(columns = ['Moradia', 'Restrição alimentar',
                                    'Usa protetor solar diariamente',
                                    'Vai na Praia Mensalmente', 
                                    'Faz Academia',
                                    'Compra e Lê Livros Todos os Anos',
                                    'Quantidade de Livros Comprados',
                                    'Autor Favorito'
                                    ])
print(df_hillo.head())


df_hillo.Streaming = df_hillo.Streaming.replace({"Todos":"Globo Play e Netflix e HBO e Disney Plus e Crunchyroll"})
df_hillo.Streaming = df_hillo.Streaming.replace({"Netflix e Disney": "Netflix e Disney Plus"})
df_hillo_stream = df_hillo['Streaming'].str.get_dummies(sep=' e ')


df_hillo = pd.concat([df_hillo, df_hillo_stream], axis=1)

print(df_hillo.head())














