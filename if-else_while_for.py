# Faça um programa que peça dois números e imprima o maior deles.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o primeiro número: "))

if numero1 > numero2:
    print(f"O maior número é: {numero1}")
elif numero2 > numero1:
    print(f"O maior número é: {numero2}")
else: 
    print("Os dois números inseridos são iguais")


## Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V - vespertino ou N - noturno.
## Imprima a mensagem de "bom dia!", "Boa tarde!" ou "Boa noite!" ou "Valor inválido!", coforme o caso. 
    
turno = input("Em qual turno você estuda: M-Matutino, V-vespertino ou N-noturno? ").upper()

if turno == 'M':
    print("Bom dia!")
elif turno == 'V':
    print("Boa tarde!")
else: 
    print("Boa noite!")


## Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
## continue pedindo até que o usuário informe um valor válido.
    
nota = float(input("Insira sua nota entre 0 à 10: "))

while nota < 0 or nota > 10:

    nota = float(input("Insira sua nota entre 0 à 10: "))

print("Nota válida!")


## Implemente um programa que classifique um aluno com base em sua pontuação em um exame. 
## O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado; 
## caso contrário, é reprovado.

nota = float(input("Insira sua nota entre 0 à 10: "))

while nota < 0 or nota > 10:

    nota = float(input("Insira sua nota do exame, entre 0 à 10: "))

if nota >= 7:
    print("Você foi aprovado!")
else:
    print("Reprovado por nota.")


## Desenvolva um programa que solicite ao usuário os comprimentos do três lados de um triângulo e classifique-o 
## como equilátero, isósceles ou escaleno. 
## equilátero: todos os lados iguais.
## isósceles: dois lados com o mesmo valor.
## escaleno: todos os lados com medidas distintas. 
    
lado1 = float(input("Insira o valor de um lado 1 do triângulo: "))
lado2 = float(input("Insira o valor de um lado 2 do triângulo: "))
lado3 = float(input("Insira o valor de um lado 3 do triângulo: "))

if lado1 == lado2 == lado3: 
    print("Triângulo equilátero, contêm todos os lados iguais.")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo isósceles, dois lados iguais.")

else: 
    print("Triângulo escaleno, todos os lados com medidas distintas.")



## Crie um programa que solicite ao usuário um login e uma senha. O programa deve permitir o acesso apenas
## se o usuário for "admin" e a senha for "admin123", caso contrário imprima uma mensagem de erro. 
    
usuario = input("Insira o nome de usuário: ").upper()
senha = input("Digite sua senha: ")

if usuario == 'ADMIN' and senha == 'admin123':

    print("Seja bem-vindo!")
    
else:
    print("Tente novamente, usuário ou senha inválidos.")


## Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente,
## adulto ou idoso. 
    
idade = int(input("Digite sua idade: "))

if idade < 0: 
    print("Idade inválida.")

elif idade >= 6 and idade <= 12:
    print("Criança.")

elif idade >= 12 and idade <= 18:
    print("Adolescente.")

elif idade >= 18 and idade <= 60:
    print("Adulto.")

else: 
    print("Idoso.")


## Criar um programa em python que solicite três números ao usuário, utilize estruturas condicionais para determinar
## o maior entre eles e apresente o resultado.
    
numero1 = float(input("Digite o número 1: "))
numero2 = float(input("Digite o número 2: "))
numero3 = float(input("Digite o número 3: "))

if numero1 > numero2 and numero1 > numero3:
    print("O número 1 é o maior. ")
elif numero2 > numero1 and numero2 > numero3:
    print("O número 2 é o maior. ")
else: 
    print("O maior número é o 3°")


## O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. O processo de leitura
## deve ser encerrado quando o usuário informar o valor zero. Certifique-se de incluir validações para garantir
## que apenas números positivos sejam considerados na contagem e cálculos. 
    


numeros_pares = 0
numeros_impares = 0

numeros_entrada = None

while numeros_entrada != 0:

    numeros_entrada = int(input("Digite um número (ou 0 para encerrar o programa)"))

    if numeros_entrada != 0:
        print("Digite apenas números positivos.")
        numero = int(numeros_entrada)

    if numero == 0:
        break

    if numero % 2 == 0:
        numeros_pares += 1

    else:
        numeros_impares += 1   

print(f"Quantidade de números pares: {numeros_pares}")
print(f"Quantidade de números ímpares: {numeros_impares}")


## Faça um programa que lê três números inteiros e os mostra em ordem crescente.


nome = input("Digite seu nome: ")

nome_upper = nome.upper()

print(nome_upper)

nome_invertido = nome_upper[::-1]

print(nome_invertido)

