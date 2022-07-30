def jogar():
    print("***************************")
    print("Jogo da Forca")
    print("************************")

    palavre_secreta = "banana"
    enforcou = False
    acertou = False


    while (not enforcou and not acertou):
        chute = input("Qual a letra?")
        chute = chute.strip()
        index = 0

        for letra in palavre_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1




    print("Fim do jogo.")
if(__name__ == "__main__" ):
    jogar()
