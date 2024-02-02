import numpy as np

## Crie um array com 4 linhas e 3 colunas com valores aleatórios
array = np.random.random((4,3))
print(array)

## Crie um array com 5 colunas e 10 linhas, inicializados com zeros.
array_zero = np.zeros((10,5))

print(array_zero)

## Crie um array com valores inteiros 3 linhas e 5 colunas com valores aleatórios

array_int = np.random.randint(0, 100, size=(3,5))

print(array_int)

## Arrays 3D

arr1_2d = np.array([[1,2],[3,4]])
arr2_2d = np.array([[2,3], [4,5]])
arr3_2d = np.array([[6,5], [5,6]])

arr_3d = np.array([arr1_2d, arr2_2d, arr3_2d])

print(arr_3d)

## Quantas dimensões tem o array (shape)

arr = np.zeros((2,4))
print(arr)

arr_shape = arr.shape
print(arr_shape)

## Flatter

arr = np.zeros((4,5))

print(arr)

arr_flat = arr.flatten()

print(arr_flat)

## Reshaping 

arr = np.array([[3,4,5], [8,11,12]])

arr_reshape = arr.reshape((3,2))
print(arr_reshape)

## Reduza o array (5,7) a apenas uma dimensão

arr1 = np.random.random((5,7))
print(arr1)

arr1_flatten = arr1.flatten()
print(arr1_flatten)

## Considere que você é uma organizadora de um jogo de bingo. Crie um array que irá representar a cartilha desses jogos de bingo. Os números das suas cartelas variam entre 1 e 30, e você terá 10 participantes. Cada cartela terá 12 números (4,3). Crie um array que representa o jogo. 



