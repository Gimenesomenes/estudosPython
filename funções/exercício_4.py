# 4. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, 
# e calcule quanto poderia comprar de cada moeda estrangeira. 

# Dólar Americano:R$4,91
#Peso Argentino:R$0,02
#Dólar Australiano:R$3,18
#Dólar Canadense:R$3,64
#Franco Suiço:R$0,42
#Euro:R$5,36
#Libra esterlina:R$6,21

def converte_dolar(carteira):
    dolar = carteira / 4.91
    return dolar

def converte_peso(carteira):
    peso = carteira / 0.02
    return peso

def converte_australiano(carteira):
    australiano = carteira / 3.18
    return australiano

def converte_canadense(carteira):
    canadense = carteira / 3.64
    return canadense

def converte_franco(carteira):
    franco = carteira / 0.42
    return franco

def converte_euro(carteira):
    euro = carteira / 5.36
    return euro

def converte_libra(carteira):
    libra = carteira / 6.21
    return libra


def main():
    print("Escolha a opção de conversão: ")
    opcao = int(input("1. Dólar Americano\n2.Peso Argentino\n3.Dólar Australiano\n4.Dólar Canadense\n5.Franco Suíço\n6.Euro\n7.Libra esterlina\n"))

    if opcao == 1: 
        carteira = float(input("Digite o valor da conversão em real (R$): "))
        resultado = converte_dolar(carteira)
        print(f"A sua conversão em Dólar Americano é: {resultado:.2f}")
    elif opcao == 2:
        carteira = float(input("Digite o valor da conversão em real (R$): "))
        resultado = converte_peso(carteira)
        print(f"A sua conversão em Peso Argentino é: {resultado:.2f} ")
    elif opcao == 3:
        carteira = float(input("Digite o valor da conversão em real (R$): "))
        resultado = converte_australiano(carteira)
        print(f"A sua conversão em Dólar Australiano é: {resultado:.2f}")
    elif opcao == 4:
        carteira = float(input("Digite o valor da conversão em real (R$): "))
        resultado = converte_canadense(carteira)
        print(f"A sua conversão em Dólar Canadense é: {resultado:.2f}")
    elif opcao == 5:
        carteira = float(input("Digite o valor da conversão em real (R$): "))
        resultado = converte_franco(carteira)
        print(f"A sua conversão em Franco Suíços é: {resultado:.2f}")
    elif opcao == 6:
        carteira = float(input("Digite o valor da conversão em real (R$): "))
        resultado = converte_euro(carteira)
        print(f"A sua conversão em Euro é: {resultado:.2f}")
    elif opcao == 7:
        carteira = float(input("Digite o valor da conversão em real (R$): "))
        resultado = converte_libra(carteira)
        print(f"A sua conversão em Libra é: {resultado:.2f}")
    else:
        print("Opção incorreta. Insira um valor real (R$)") 


if __name__ == "__main__":
    main()