# o que são listas

lista_frutas = []

fruta = input("Digite sua fruta: ")

lista_frutas.append(fruta)

# o que são tuplas
# a diferença entre tuplas e listas, é que em tuplas os valores não podem ser alterados.

tupla = ('maçã', 'uva')
print(tupla)


## Dicionários armazenam pares chave-valor, onde cada valor é associado a uma chave única. 

dicionario = {}
dicionario['maça'] = 'É uma fruta'
dicionario['carro'] = 'É um veículo'
dicionario['Gato'] = 'É um animal'

print(dicionario)
 

## Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
## O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
## Se a pessoa responder positivamente a 2 questões ela deve ser classificada como Suspeita, 
## entre 3 e 4 como Cúmplice e 5 como Assassino.
## Caso contrário, ele será classificado como Inocente.


perguntas = [
    'Telefonou para a vítima?',
    'Esteve no local do crime?',
    'Mora perto da vítima?',
    'Devia para a vítima',
    'Já trabalhou com a vítima?'
]

respostas_positivas = 0

for pergunta in perguntas:

    resposta = input(pergunta + " sim ou não : ").lower()

    if resposta == 'sim':
        respostas_positivas += 1

if respostas_positivas == 2:
    print("Você é Suspeita(a) do crime.")

elif respostas_positivas == 3 or respostas_positivas == 4:
    print("Você é cúmplice do crime.")

elif respostas_positivas == 5:
    print("Você é assassino do crime. ")

else:
    print("Você é inocente.")

## Faça um programa que peça as quatro notas de 5 alunos, calcule
## e armazene numa lista a média de cada aluno, imprima o número
## de alunos com média maior ou igual a 7.0

medias_alunos = []
notas = []


for i in range(5):
   
    for j in range(4):
   
        nota = float(input(f"Insira suas 4 notas. Nota {j + 1} do aluno {i + 1} "))
        notas.append(nota)

        #print(notas)
    
    media_aluno = sum(notas) / len(notas)
    medias_alunos.append(media_aluno)
    print(medias_alunos)

for i, media in enumerate(medias_alunos, start=1):
    if media >= 7.0:
        print(f"O aluno {i} foi aprovado.")
    else:
        print(f"O aluno {i} foi reprovado.")


## Crie um dicionário representando um carrinho de compras. 
## Adicione produtos (chaves) e quantidade (valores) ao carrinho.
## Calcule o total de compra do carrinho.
        

compras = {
    'Maçã': 3.20,
    'Banana': 6.90,
    'Macarrão': 3.98,
    'Molho': 2.76,
    'Pão': 6.00,
    'Queijo': 10.00

}

valor_da_compra = 0

for valor in compras.values():

    valor_da_compra += valor

print(f"O valor total da compra é: {valor_da_compra:.2f}")


## Crie um dicionário representando contatos (nome, telefone);
## Permita ao usuário procurar por um contato pelo nome.

agenda = {
    'Carolina':'99628-0243',
    'Lucas': '99323-0394',
    'Isabela': '99878-0923',
    'Ana Carolina': '99823-3045'
}


contato = input("Insira o nome que quer procurar na agenda: ")

## verifica se o nome está na agenda de contatos
if contato in agenda:

    ## atribui um telefone
    telefone = agenda[contato]
    print(f"O numero de telefone de {contato} é: {telefone}")
else:
    print(f"Esse nome {contato}, não consta na sua agenda.")


## Crie duas tuplas. Concatene-as para fomar uma nova tupla.
    
tupla1 = ('maçã', 'uva', 'morango', 'cupuaçu')
tupla2 = ('vemelha', 'roxa', 'vemelho', 'branco')

tupla_concatenada = tupla1 + tupla2

print(tupla_concatenada)


## Faça um programa que permita ao usuário digitar o seu nome e em seguida
## mostre o nome do usuário de trás para frente
## utilizando somente letras maiúsculas. Dica: lembre-se
## que ao informar o nome o usuário pode digitar letras maiusculas ou minusculas.


nome = input("Digite seu nome: ")

nome_upper = nome.upper()

print(nome_upper)

nome_invertido = nome_upper.join(reversed(nome_upper))

print(nome_invertido)
