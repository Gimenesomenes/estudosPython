# importante blibliotecas
import pandas as pd
import numpy as np
# bibliotecas para visualização de dados
import seaborn as sns
import matplotlib.pyplot as plt
# bibliotecas para estatística
import scipy.stats as stat

# utilizando biblioteca que contêm vários DataFrames
from pydataset import data

#iniciando a leitura dos dados

forbes = data('Forbes2000')
# Verificando o DataFrame
#print(forbes.head())

# Observando que tipo de variáveis encontramos no DataFrame
#print(forbes.info())

# Rank é uma variável numérica e sales, profits, assets, marketvalue são categóricas, assim como name, country e category.

# Análise de tendência central 

# Moda
moda = forbes.iloc[:, 2:8].mode()
print(moda)

# Média
media = forbes[['sales','profits','assets','marketvalue']].mean()
print(media)

# Mediana

mediana = forbes[['sales','profits','assets','marketvalue']].median()
print(mediana)

# Utilizando describe para calcular estatísticas descritivas das variáveis numéricas

describe = forbes[['sales','profits','assets','marketvalue']].describe()
print(describe)


# Análise de dispersão e outliers
# 1. Amplitude, desvio padrão e variancia
# 2. Analisar os histogramas das variáveis
# 3. Construir o boxplot
# 4. Verificar outliers 

def describe_new(df):
    df1 = df.describe()
    df1.loc['amplitude'] = df1.loc['max'] - df1.loc['min']
    df1.loc['variancia'] = df1.loc['std']*df1.loc['std']
    return df1

print(describe_new(forbes))

# Montando os histogramas

plt.rcParams['figure.figsize'] = [8, 10]
sns.set_theme()
# criando vários gráficos
for column in forbes.select_dtypes(include=np.number).columns:
    plt.figure()
    sns.displot(data = forbes, x = column, kde= True)
    plt.title("Histograma: "+column)
    plt.show()


# Boxplot das variáveis
    
plt.rcParams['figure.figsize'] = [8, 4]
sns.set_theme()
#criando vários gráficos
for column in forbes.select_dtypes(include=np.number).columns:
    plt.figure()
    sns.boxplot(data = forbes, x = column, color='cyan', showfliers=True)
    plt.title("Boxplot: "+column + " in billion USD")
    plt.show()

# Pelos box plots podemos ver a grande concentração de empresas com:
# vendas proximas a 2-9 bilhoes
# Lucro oscilando proximo a 0 (0.1 a 0.5 bilhões) com valores positivos e negativos nas caldas.
# Assets (ativos) de 5 a 25 bilhões
#Valores de mercado próximo a 3-11 bilhões
    
# Vamos analisar os outliers encontrados
    
#1. Método do Z-score:

def find_outliers_zscore(dataset, threshold, colname):
    df = dataset[colname]
    outliers = []
    zscore = []
    threshold = threshold
    mean = np.mean(df)
    std = np.std(df)
    for i in df.values:
        z_score = (i - mean)/std 
        zscore.append(z_score)
        if np.abs(z_score) > threshold:
            outliers.append(i)
    print("o número de outliers encontrado em {} foi de:" .format(colname), len(outliers))
    return zscore, outliers

for column in forbes.select_dtypes(include=np.number).columns:
    zscore, out = find_outliers_zscore(forbes, 3, column)
    if len(out) > 0:
        plt.figure(figsize= (10,5))
        sns.displot(zscore)
        plt.axvspan(xmin=3, xmax= max(zscore), alpha=0.2, color='red')
        plt.title("Outliers detectados em {}" .format(column))
        plt.show()


def replace_outliers_zscore(dataset, threshold, colname):
    df = dataset[colname]
    outliers = []
    zscore = []
    val = []
    threshold = threshold
    mean = np.mean(df)
    std = np.std(df)
    for i in df.values:
        z_score = (i - mean)/std 
        zscore.append(z_score)
        if np.abs(z_score) > threshold:
            outliers.append(i)
            val.append(np.nan)
        else:
            val.append(i)
    return val

def drop_outliers(dataset, threshould):
    for column in dataset.select_dtypes(include=np.number).columns:
        dataset[column] = replace_outliers_zscore(dataset, 3, column)
    return dataset.dropna()

def replace_median_outliers(dataset, threshould):
    for column in dataset.select_dtypes(include=np.number).columns:
        dataset[column] = replace_outliers_zscore(dataset, 3, column)
    return dataset.fillna(dataset.median())

forbes_zscore_na = drop_outliers(forbes, 3)
forbes_zscore_median = replace_median_outliers(forbes, 3)

print(forbes_zscore_median)