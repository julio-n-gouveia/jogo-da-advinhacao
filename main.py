import random

print("Bem vindo ao jogo de adivinhação!")

numero_secreto = 42

total_tentativas = 3
rodada = 1

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

print("Fim de jogo.")