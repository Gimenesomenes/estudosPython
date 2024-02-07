# O que é pandas? 

> O pandas, é um pacote dedicado à manipulação de dados, também possuí funcionalidades para a visualização de dados. Sua estrutura é fundamentada em dois pacotes essenciais do Python: NumPy e Matplotlib. Enquanto o NumPy oferece objetos de matriz multidimensional para facilitar a manipulação de dados, o Matplolib proporciona ao pandas capacidades robustas de visualização de dados.

## Introdução ao Data Frame
> DataFrames são o coração do pandas. 
Agregação de Dados para Insights:
>Discussão sobre como combinar dados para uma compreensão mais aprofundada. 
Guardar informações pode ser feito de muitas maneiras, mas a mais comum é como uma tabela, que chamamos de "dados retangulares" ou "dados tabulares". 

### formas de criar um dataframe
>Podemos criar um dataframes de várias formas, umas da mais simples é utilizzando dicionários e listas.


##  Lendro um arquivo e transformando-os em DataFrame

# csv

>df_csv = pd.read('arquivo.csv')

# excel

>df_excel = pd.read_excel('planilha.xlsx 'sheet_name='nome_da_planilha')

# json

>df_json = pd.read_json('arquivo.json')

# parquet

>df_parquet = pd.read_parque('arquivo.parquet')

# SQL

>from sqlalchemy import create_engine

>engine = create_engine('sqlite:///banco_de_dados.db')
>query = 'SELECT * FROM tabela'
>df_sql = pd.read_sql(query,engine)


## Primeiros métodos para entender seu dataframe

> df.head ()

O pandas tem um truque chamado "head" que mostra as primeiras linhas da tabela. Se tiver muitas linhas, isso ajuda bastante!

> df.info()

Tem um jeito do pandas nos contas os nomes das colunas, que são como etiquetas, e se tem alguma informação faltando, ele usa um método chamado "info" para isso.


> df.shape()

A tabela do pandas tem um jeito de mostrar quantas linhas e quantas colunas ela tem, como se fosse um resuminho. 

> df.describe()

O pandas também sabe fazer as contas! Com o "describe", ele conta coisas legais sobre os números na tabela, tipo média e mediana. Ele até fala quantos números tem em cada coluna. 

## Peças Especiais do DataFrame

A tabela do pandas é como um quebra-cabeça como três partes:

> <b>.values:</b> os valores (que são dados mesmo);

> <b>.columns:</b> as etiquetas (labels) das colunas;

> <b>.index: </b> etiquetas das linhas;

Isso ajuda entender melhor cada pedacinho!


## Ordenação e subconjuntos

Você pode ordenar as linhas usando o método <b>sort_values</b>, passando o nome da coluna pela qual você deseja ordenar...

> df.sort_values('coluna')


## Métodos extração estatística

> .median() - Calcula a mediana de um conjunto de dados, indicando o valor central quando os dados estão ordenados.

> .mode() - identifica o(s) valor(es) mais frequente(s) e um conjunto de dados.

> min()

> max()

> .var() - variância, uma mediana da dispersão dos dados.

> .std() - Calcula o desvio padrão, indicando a dispersão média dos dados em relação à média.

> .sum() - Soma todos os valores em um conjunto de dados.

> .quantile() - Calcula um percentil específico em um conjunto de dados, indicando o valor abaixo do qual uma determinada porcentagem dos dados está.


## Métodos de somas acumuladas

> .cumsum() - Calcula a soma cumulativa, fornecendo uma série de valores acumulados à medida que percorre o conjunto de dados.

> .cummax() - máximo cumulativo

> .cummin() - mínimo cumulativo

> .cumprod() - produto cumulativo

### excluindo duplicados

> .drop_duplicates()


### values_count()

> O método values_count(), retorna uma contagem de valores únicos em uma coluna de um DataFrame, fornecendo uma série que lista os valores distintos junto com a frequência e cada valor.

<b>normalize</b> é um argumento opcional que, quando definido como True, retorna as proporções normalizadas em vez das contagens absolutas. Ele apresenta porcentagem relativa de cada valor em relação ao total de observações. 

> .values_count(normalize=True)


### Agrupamento de dados

> .groupby() - no Pandas é utilizado para agrupar um DataFrame por uma ou mais colunas, permitindo a aplicação de operações em cada grupo separadamente. Ele cria um objeto de grupo que pode ser combinado com várias funções de agregação, como média, mediana, soma, minimo, max.. Esse método é frequente usado em conjunto com outros métodos, como <b>agg</b>, para calcular estatísticas resumidas para cada grupo de dados. 


> pivot_table(values = , index = )


### O que é slicing? 

> Slicing é uma técnica para selecionar elementos consecutivos de objetos. Você também pode cortar DataFrames, mas primeiro precisa ordenar o índice.


### Visualizando um agrupamento de dados 

> media = df.groupby('Raça')['Peso'].mean()
> media.plot(kind='bar')

## Dados não vem perfeitos

> Você pode receber um DataFram com valores ausentes, por isso é importante saber como lidar com eles. A maioria dos dados não é perfeita - sempre existe a possibilidade de que faltem algumas peças no seu conjunto de dados. Em um DataFrame do pandas, os valores ausentes são indicados com N-a-N, que significa "não é um número".

### Detectando valores nulos

> .isna()


### Removendo dados nulos

O método <b>dropna</b> no pandas é utilizado para remover linhas ou colunas de um DataFrame que contenham valores nulos (NaN), facilitando a limpeza e preparação dos dados. Ele pode ser aplicado para remover linhas com pelo menos um NaN (padrão) ou colunas específicas, proporcionando flexibilidade na manipulação de conjuntos de dados. 



