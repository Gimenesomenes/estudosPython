''' 6. Vamos construir um jogo de forca.O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida.
A palavra secreta será representada por espaços em branco,um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas.Em cada tentativa,o jogador pode fornecer uma letra.
Se a letra estiver presente na palavra secreta,ela será revelada nas posições correspondentes.Se a letra não estiver na 
palavra,uma mensagem de erro deverá ser informada. Após um número máximo de erros,o jogador perde.
O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.
Dica:Você precisará importar uma biblioteca para resolver esse exercício '''



import random


def jogo_forca():

    lista_palavras = ['Futebol', 'Basketball', 'Tenis',  'Curling', 'Salto', 'Volei', 'Judô', 'Skate']
    random.shuffle(lista_palavras)
    lista_palavras = (lista_palavras[0]).upper()
    letras_acertadas = ("_" * len(lista_palavras))
    print(letras_acertadas)
    letras_certas = (list(letras_acertadas))
    print(letras_certas)

    enforcou = False
    escapou = False
    tentativas = 1

    while(tentativas <= 6):
        print(f"A lista de palavras é relacionada a esporte, o esporte tem {len(lista_palavras)}. \n")
        chute = input("chute uma letra: ")
        chute = chute.strip().upper()


        if chute not in lista_palavras:
            tentativas += 1
            print(f"Você ainda tem {len(lista_palavras) - tentativas + 1} para jogar.")
        else:
            posicao = 0
            for letra in lista_palavras:
                if(chute == letra):
                    letras_certas[posicao] = letra
                posicao += 1 
        # Metodo para quantidade de tentativas ser do tamanho do pais secreto
        enforcou = tentativas > len(lista_palavras)
        if(enforcou == True):
            print("Você se enforcou")
        print(letras_certas)

        # Metodo para transformar a lista em uma string e finalizar o jogo quando o pais for completo
        acertou = ''.join(letras_certas)
        if(acertou == lista_palavras):
            print("\n", "Parabéns, você escapou da forca!")
            break
if(__name__ == "__main__"):
    jogo_forca()