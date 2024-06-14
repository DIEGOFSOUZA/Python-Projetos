import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvedor", "computador", "inteligencia", "algoritmo"]
    return random.choice(palavras)

def exibir_estado(palavra, letras_adivinhadas):
    estado = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            estado += letra + " "
        else:
            estado += "_ "    
    return estado.strip()  

def jogo_da_forca():
    palavra = escolher_palavra()      
    letras_adivinhadas = []
    tentativas_restantes = 6
    adivinhou_palavra = False

    print("Bem vindo ao Jogo da Forca")
    print(f"A palavra tem {len(palavra)} letras.")
    print(exibir_estado(palavra,letras_adivinhadas))

    while not adivinhou_palavra and tentativas_restantes > 0:
        tentativa = input("Adivinhe uma letra: ").lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, insira uma unica letra.")
            continue

        if tentativa in letras_adivinhadas:
            print("Voce ja adivinhou esta letra.")
            continue

        letras_adivinhadas.append(tentativa)

        if tentativa in palavra:
            print("Esta letra existe. Parabéns!")
        else:
            print("Que pena...esta letra não contém.")
            tentativas_restantes -= 1

        estado_atual = exibir_estado(palavra, letras_adivinhadas)
        print(estado_atual)
        print(f"Tentativas restante: {tentativas_restantes}") 

        if "_" not in estado_atual:
            adivinhou_palavra =  True

    if adivinhou_palavra:
        print("Parabéns! Voce adivinhou a palavra!")    
    else:    
        print(f"Que pena! Voce perdeu! A Palavra era '{palavra}'.")    

if __name__ == "__main__":
    jogo_da_forca()
                