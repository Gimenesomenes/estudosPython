import pandas as pd 
import numpy as np 

# Uma influenciadora digital de bem estar gostaria de analisar possíveis empreendimentos dentro de diferentes propostas que recebe.
# Essas propostas podem ser excludentes ou somatórias.

df = pd.read_csv('research people.csv')

print(df.columns)

df_influence = df.drop(columns='Unnamed: 0')

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

df_influence.rename(columns=novas_cols, inplace=True)
print(df_influence.columns)