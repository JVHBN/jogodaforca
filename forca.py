import random

def escolhe_palavra():
    palavras = ["python", "programacao", "linguagem", "computador", "software"]
    return random.choice(palavras)

def jogo_da_forca():
    palavra = escolhe_palavra()
    letras_descobertas = ["_" for _ in palavra]
    tentativas = 25
    letras_tentadas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra: " + " ".join(letras_descobertas))

    while tentativas > 0 and "_" in letras_descobertas:
        letra = input("Digite uma letra: ").lower()
        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_tentadas.append(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_descobertas[i] = letra
            print("Correto! Palpite: " + " ".join(letras_descobertas))
        else:
            tentativas -= 1
            print(f"Incorrente! Tentativas restantes: {tentativas}")

    if "_" not in letras_descobertas:
        print("Parabéns! Você venceu!")
    else:
        print(f"Fim de jogo. A palavra era: {palavra}")

jogo_da_forca()
