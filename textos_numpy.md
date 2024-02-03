# Porque usar numpy e não listas? 

> <b>Arrays Numpy</b> aceita que todos os elementos sejam diferentes tipo de dados, contudo o array sempre terá apenas um tipo de dados*. Contudo a normal dentro da análise de dados que usamos <b> apenas um tipo de dados dentro de um array </b>

> Um único tipo de dados também resulta em arrays NumPy ocupando <b> menos espaço na memória</b> em comparação com listas. 

> Quando precisamos de uma <b> estrutura multidimensional </b> para armazenar os dados, optamos por arrays em vez de listas, pois as listas podem ser unidimensionais apenas. 

> Se precisarmos de um comprimento fixo e alocação estática, usamos arrays em vez de listas.

> Quando é necessária um processamento de dados mais rápido, preferimos arrays em vez de listas. 

> Tipos de dados primitivos podem ser armazenados diretamente em arrays, mas não em listas. 

## Dimensões do array (atributos e métodos)

### Atributo: 
> .shape

### método:
> .flatten()
> .reshape()


## nomenclatura

>np.array(x,y)

>onde x = n° de linhas e y = n° de colunas no vetor.

>np.concatenate() -> concatenar vetores

>np.delete(array, 2, axis = 0)

2 -> é o n° da linha do vetor que será eliminada e axis = 0 é o eixo, sendo [0] sempre o primeiro eixo 


## Calculos com array

array.sum() -> soma o array inteiro

array.sum(axis=0) -> vai somar todas as linhas do array 

array.sim(axis=1) -> soma as colunas do array

## Porque usar arquivos .npy

> Eficiência de armazenamento: Especialmente útil para grande números de dados, reduzindo o requisito de espeços necessários e melhorando a velocidade de operaçao.

> Preservação de informações: inclui informações cruciais do tipo de dados e a forma do array. Possibilitando o carregamento original do array, evitando perda de informações.

> Carregamento rápido: geralmente mais rápido do que formato de textos

> Compatibilidade com Numpy: o formato .npy é específico do NumPy, proporcionando compatibilidade sólida com outras ferramentas e bibliotecas baseadas em NumPy.  
