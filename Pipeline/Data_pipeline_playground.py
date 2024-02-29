import requests
import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#from wordcloud import WordCloud

# API

headers = {"chave-api-dados":"9548fe7a0337f8d380af71a482695860"}

# Acesso ao portal da transparência do governo federal 

#url = 'https://api.portaldatransparencia.gov.br/api-de-dados/emendas?ano=2022&pagina=2'

#resposta_ = requests.get(url, headers=headers)

#data1 = resposta_.json()

#data2 = resposta_.json()

#print(pd.DataFrame(data2))

url = 'https://api.portaldatransparencia.gov.br/api-de-dados/emendas?ano=2022&pagina='

# Emendas até a página 408

list_urls = []
for i in range(1,409):

    list_urls.append(url + str(i))

#print(list_urls)
    
def run_request(url_):
    resposta = requests.get(url_, headers=headers)
    return resposta.json()

 #   print(resposta.json())

vec_run = np.vectorize(run_request)

arr_urls = np.asarray(list_urls)

arr_response = vec_run(arr_urls)

#print(arr_response)

conc_lists = np.concatenate(arr_response).tolist()
df = pd.DataFrame(conc_lists)

print(df.info())