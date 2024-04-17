
# 1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))


def soma(num1, num2, num3):

    resultado = num1 + num2 + num3
    

    return resultado

print("A soma dos três números é:", soma(num1, num2, num3))

# 2. Reverso do número.Faça uma função que retorne o reverso de um número inteiro informado.Por exemplo: 127->721.


num_int = int(input("Insira um número inteiro: "))      # Entrando com a variável no programa 

def reverso(num_int):       # Criando função com nome reverso e recebendo argumento num_int

    num_str = str(num_int)      # Transformando o número em string para inverter
    numero_invertido = num_str[::-1]       # Invertendo a string 
    
    return numero_invertido         # Retorna o número invertido
    
num_invertido = reverso(num_int)        # Chamando a função reverso

print(f"O número inserido foi: {num_int} e seu inverso: {num_invertido}")       # mostrando o resultado na tela

# 3. Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou 
# vice-versa. Para cada opção,crie uma função.

# Plus:Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão 
# correta.

def celsius_to_fahrenheit(celsius):
    
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    print("Escolha uma opção")
    opcao = int(input("1.Coverter de Celsius para Fahrenheit. \n2. Converter de Fahrenheit para Celsius.\n"))

    if opcao == 1:
        celsius = float(input("\nDigite a temperatura em Celsius: "))
        resultado = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {resultado:.2f}°F")
    elif opcao == 2:
        fahrenheit = float(input("\nDigite a temperatura em Fahrenheit: "))
        resultado = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F é igual a {resultado:.2f}°C")
    else:
        print("Opção inválida. Tente novamente!")

if __name__ == "__main__":
    main()



