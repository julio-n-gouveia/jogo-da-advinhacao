import forca
import Adivinhacao

print("***************************")
print("Seleção de jogos")
print("************************")

print("Forca (1)  Adivinhação (2)")

jogo = int(input("Escolha um dos jogos: ")

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando Adivinhação")
    Adivinhacao.jogar()