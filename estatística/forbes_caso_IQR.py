## Caso forbes utilizando IQR

# importante blibliotecas
import pandas as pd
import numpy as np
# bibliotecas para visualização de dados
import seaborn as sns
import matplotlib.pyplot as plt
# bibliotecas para estatística
import scipy.stats as stat
# tratando valores faltantes
import missingno as msno

# utilizando biblioteca que contêm vários DataFrames
from pydataset import data

forbes = data('Forbes2000')

def find_outlier_iqr(dataset, colname):
    q25, q75 = np.quantile(dataset[colname], 0.25), np.quantile(dataset[colname], 0.75)
    # calcula iqr
    iqr = q75 - q25
    # calcular outlier cutoff
    cut_off = iqr * 1.5
    #calcula margens inferiores, lower e superiores upper
    lower, upper = q25 - cut_off, q75 + cut_off
    print("IQR é: ", iqr)

    outliers = []

    for i in dataset[colname].values:
        if((i > upper) or (i < lower)):
            outliers.append(i)

    print("O número de outliers encontrado foi de", len(outliers))
    return lower, upper, outliers

for column in forbes.select_dtypes(include=np.number).columns:
    lower, upper, out = find_outlier_iqr(forbes, column)
    if(len(out) > 0):
        plt.figure(figsize= (10,6))
        sns.displot(forbes[column], kde=False)
        plt.axvspan(xmin = lower, xmax = forbes[column].min(), alpha=0.2, color='red')
        plt.axvspan(xmin= upper, xmax = forbes[column].max(), alpha=0.2, color='red')
        plt.title("Outliers detectador em {}".format(column))
#        plt.show()

# análise de missing values (dados faltantes)
        
missing = forbes.isna().sum()

missing_perc = 100 * forbes.isna().sum() / len(forbes)

mis_val_table = pd.concat([missing, missing_perc], axis=1)

mis_val_table = mis_val_table.rename(columns = {0: "# Count: valores nulos", 1 : "% do Total"})

mis_val_table = mis_val_table[mis_val_table.iloc[:, 1] != 0].sort_values(
'% do Total', ascending=False).round(1)

print("O dataframe contém " + str(forbes.shape[1]) + " colunas. \n"
        "contendo " + str(mis_val_table.shape[0]) + " colunas com valores faltantes.")

print(mis_val_table)
 



    