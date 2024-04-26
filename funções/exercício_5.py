# 5. Crie uma função chamada contar_vogais que recebe uma string como parâmetro.Implemente a lógica para contar 
# o número de vogais na string e retorne o total de vogais.Solicite ao usuário para inserir uma frasee utilize a 
# função para contar as vogais.

def contar_vogais(frase):

    vogais = "aeiouAEIOU"
    cont = 0

    for char in frase:
        if char in vogais:
            cont += 1
    return cont

frase = input("Insira uma frase: ")
total_vogais = contar_vogais(frase)

print(f"A frase '{frase}' contém {total_vogais} vogais.")