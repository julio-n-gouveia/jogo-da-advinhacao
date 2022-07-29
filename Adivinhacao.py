import random
def jogar():
    print("***********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("***********************************")

    numero_secreto = round(random.randrange(1,101))
    total_tentativas = 0

    print("Qual nivel de dificuldade ?")
    print("Cadete (1) Espartano (2) Rei Leonidas (3)")
    nivel = int(input("Escolha: "))

    if(nivel == 1):
        total_tentativas = 20
        print("Vamos lá. Cadete!")

    elif(nivel == 2):
        total_tentativas = 10
        print("Vamos lá, Espatano!")

    else:
        total_tentativas = 5
        print("Vamos lá, Meu Rei!")

    for rodada in range (1, total_tentativas + 1) :
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 0 e 100! Eu, hein...")
            continue

        maior = chute > numero_secreto
        menor = chute < numero_secreto
        acertou = numero_secreto == chute

        if (acertou):
                print("Você Acertou!")
                break
        else:
            if(maior):
                print("Leonidas: Um pouco menos...")
            elif(menor):
                print("Leonidas: Um pouco mais...")

        if(rodada == total_tentativas):
            print("THIS IS SPARTA! PERDEU!")

    print("Fim de jogo.")

if(__name__ == "__main__"):
    jogar()
