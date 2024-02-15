import numpy as np

## Explorando ecossistemas:
## Como bióloga marinha, me encontrei em uma expedição nas profundezas do Oceano Pacífico,
## onde estávamos estudando a biodiversidade e a saúde dos recifes de coral. O catálogo abaixo demonstra
## dados das espécies encontradas, considere a seguinte ordem de colunas:

especies=np.array([[747,89,33,5],
                   [623,123,32,13],
                   [501,22,49,2],
                   [116,101,42,10],
                   [297,56,69,22],
                   [613,64,27,7],
                   [295,84,29,14],
                   [692,105,72,16],
                   [229,103,35,5],
                   [374,124,70,1]])

# a) Selecione a segunda coluna  com a qtade de espécies encontradas e adicione em um array as qtd_especies.

qtd_especies = especies[:, 1]
print(qtd_especies)

# b) De qtd_especies selecione apenas as primeras 3 quantidades e print. 

print(qtd_especies[0:3])

# c) print as 5 últimas quantidades de espécies. 

print(qtd_especies[:-5])

# d) Crie um array que contenha apenas os tamanhos das espécies e orderne por ordem crescente. 

tam_especies = especies[:, 3]
print(tam_especies)

## ordena ordem crescente

organiza = np.sort(tam_especies)
print(organiza)

## ordena ordem descrescente 

de_organiza = np.sort(tam_especies)[::-1]
print(de_organiza)


## Filtrando arrays

pessoas_id_idade = np.array([1, 2, 3, 4, 5])

# utilizando máscaras
mask = pessoas_id_idade % 3 == 0 
print(mask)

fancy = pessoas_id_idade[mask]
print(fancy)

pessoas_id_idade = np.array([[1,22], [2,21], [3,27], [4,26]])
print(pessoas_id_idade)

idade_21 = np.where(pessoas_id_idade >= 21, "maior idade", pessoas_id_idade)
print(idade_21)

## Ainda usando o array de espécies marítimas,

# Usando um index booleano crie um array que contém os dados da maior espécie encontrada
# (considerando o seu tamanho), esse valor corresponde ao valor 22. 

especies=np.array([[747,89,33,5],
                   [623,123,32,13],
                   [501,22,49,2],
                   [116,101,42,10],
                   [297,56,69,22],
                   [613,64,27,7],
                   [295,84,29,14],
                   [692,105,72,16],
                   [229,103,35,5],
                   [374,124,70,1]])

especie_maior = especies[:, 3] == 22

print(especie_maior)

## usando o fancy index faça um array que contém apenas dados da espécie com ID 297

mask_especie = especies[:, 0] == 297
print(mask_especie)

fancy_especies = especies[mask_especie]
print(fancy_especies)


## Usando np.where() faça um array com a linha com dados correspondentes a espécie com 105 representantes encontrados.

especie_105 = np.where(especies[:, 1] == 105)
especie_105 = especies[np.where(especies[:, 1] == 105)]
print(especie_105)


## Considere a profundeza em que a espécie foi encontrada substitua valores maiores que 60 com "profundo"


profundeza = np.where(especies[:, 2] > 60, "Profundo", especies[:, 2])

print(profundeza)

## Exerc. concatenação

cartela_bingo = np.random.randint(1, 31, size=(4, 4))
print(cartela_bingo)

cartela1 = cartela_bingo[:3]
print(cartela1)

cartela2 = cartela_bingo[-1:]
print(cartela2)

conc_array = np.concatenate((cartela1, cartela2))
print(conc_array)

cartela_bingo == np.concatenate((cartela1, cartela2))

## Calculos com array

sala_espera = np.array([['5','30','1','Alice'],
                        ['6','29','1','Bob'],
                        ['7','35','3','Cristina'],
                        ['8','34','3','Luiz']
])
print(sala_espera)

array_del = np.delete(sala_espera, 3, axis=0)
print(array_del)

## Ainda no conjunto espécies adicione: [[204,10,40,12],[392,11,81,11]]

#print(especies)

array_add = np.array([[204,10,40,12], [392,11,81,11]])
print(array_add)

array_conc_espec = np.concatenate((especies, array_add))
print(array_conc_espec)

## Adicione mais uma coluna no array original, agora com o número de espécies encontradas que indica se o animal enxerga
## ou não

array_visao = np.array([0,1,0,0,0,0,1,0,1,1])
#print(array_visao)
reshape_visao = np.array([0,1,0,0,0,0,1,0,1,1]).reshape((10,1))
#print(reshape_visao)

array_conc_visao = np.concatenate((especies, reshape_visao), axis=1)
print(array_conc_visao)