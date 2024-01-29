# Faça um programa que peça dois números, realize as principais operações
# soma, subtração, multiplicação e divisão.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


resultado1 = numero1+numero2

print(f"O resultado da soma é: {resultado1:.2f}")

resultado2 = numero1-numero2

print(f"O resultado da substração é: {resultado2:.2f}")

resultado3 = numero1/numero2

print(f"O resultado da divisão é: {resultado3:.2f}")

resultado4 = numero1*numero2

print(f"O resultado da multiplicação é: {resultado4:.2f}")



## Peça ao usuário para informar o ano de nascimento. Em seguida calcule e imprima a idade atual.

nascimento = int(input("Informe o ano de seu nascimento: "))

idade_atual = (2024 - nascimento)

print(f"A sua idade atual é: {idade_atual}")


## Faça um programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros

km = float(input("Informe a quantidade de Km percorridos: "))

metros = km*1000
centimetros = metros*100
milimetros = centimetros*10

print(f"A quantidade em metros é: {metros:.2f}")
print(f"A quantidade em centímetros é: {centimetros:.2f}")
print(f"A quantidade em milímetros é: {milimetros:.2f}")



## Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida
## Calcule e imprima o consumo médio em km/l.

litros = float(input("Digite a quantidade de litros consumidos: "))
distancia = float(input("Digite a distância percorrida: "))


km_l = distancia / litros

print(f"O consumo médio é: {km_l} Km/l")


## Escreva um programa que calcule o tempo de uma viagem. Faça um 
## comparativo do mesmo percurso de avião, carro e ônibus.
## avião = 600km/h
## carro = 100km/h
## ônibus = 80km/h

distancia = float(input("Informe a distância a ser percorrida em Km: "))

aviao = 600
carro = 100
onibus = 80

tempo_aviao = distancia / aviao
tempo_carro = distancia / carro
tempo_onibus = distancia / onibus

print(f"O tempo do percurso de avião seria, {tempo_aviao} horas.")
print(f"O tempo do percurso de carro seria, {tempo_carro} horas.")
print(f"O tempo do percurso de onibus seria, {tempo_onibus} horas")


## Solicite ao usuário o peso em kg e a altura em metros. 
## Calcule e imprima o Indice de Massa Corporal (IMC) usando a fórmula. IMC = peso / (altura*altura)

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

IMC = peso / (altura*altura)

print(f"O seu IMC corresponde a: {IMC:.2f}")

if IMC < 18.5: 
    print("Baixo peso.")

elif IMC >= 18.5 and IMC <= 24.99:
    print("Normal.")
elif IMC >= 25 and IMC <= 29.99:
    print("Sobrepeso")

else:
    print("Obesidade.")


## Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
## Calcule e mostre o total do seu salário no referido mês.

valor_trabalho = float(input("Qual o valor da sua hora trabalhada ? "))
hora_mes = float(input("Qual o número de horas trabalhadas ? "))


total_salario = (valor_trabalho * hora_mes)

print(f"O valor do seu salário mensal é: {total_salario:.2f}")

## Solicite ao usuário o número de horas de exercícios físico por semana.
## Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minutos.

horas_exercicios = float(input("Informe o número do horas de exercícios físico na semana: "))

minutos = (horas_exercicios * 4) * 60

calorias_gastas = (minutos * 5)

print(f"A quantidade de calorias (cal) gasta em um mês é: {calorias_gastas:.2f}")
