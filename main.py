############### Blackjack Project #####################
import jogo
import calculos
import arts
import random

continuar = True
blackjack = False


comecar_jogo = input("Você quer jogar 21? (S ou N)\n")

if comecar_jogo.upper() == "S":

    print(arts.logo)
    print("Seja bem vindo... *barulhinhos de carta* ")

    calculos.aposta2 = random.randint(1, 100)
    print("O computador apostou R$" + str(calculos.aposta2))

    valido = False
    while valido == False:
        calculos.aposta1 = input("Qual valor você quer apostar?\n")
        if calculos.aposta1.isnumeric() == False:
            print("Vamos lá... Estou falando de valores reais.")
        else:
            valido = True

    jogo.comecar()
    #Checar se ocorreu um blackjack
    if jogo.blackjack(continuar) == False:
        continuar = False
        blackjack = True

    #Definir decks para melhoria de código
    deckJogador = jogo.deck1
    deckComputador = jogo.deck2

    while continuar == True:
        #Checar se existe soma maior que 21 pontos, por uma carta 11. Substituindo por 1
        jogo.somar(deckJogador)
        jogo.somar(deckComputador)
        print(f"Suas cartas são: {deckJogador} - você tem {jogo.somar(deckJogador)} pontos\n"
              f"A carta face do computador é: {deckComputador[0]}")

        sortear = input("Você quer tirar uma carta? Se não, passa sua vez... (S ou N)\n")

        if sortear.upper() == "S":
            jogo.sortear(deckJogador) #Sorteia a carta
            if jogo.blackjack(continuar) == False: #Se acontecer um blackjack, para o jogo
                break
                blackjack = True
            if jogo.checarValores(continuar) == False:
                break
            else:
                if jogo.checarValores(continuar) == False: #Se o deck acumular 21 pontos, vence.
                    break
        elif sortear.upper() == "N":
            while jogo.somar(deckComputador) < 17: #Computador joga enquanto tem menos de 16 pontos
                jogo.sortear(deckComputador)
                jogo.somar(deckComputador)
            continuar = False
        else:
            print("Acha que estou para brincadeira? Não entendi o que disse. Saia agora!")
            continuar = False

    if blackjack != True:
        jogo.fim() #Finaliza o jogo


elif comecar_jogo.upper() == "N":
    print("Tudo bem... volte quando estiver pronto!")

else:
    print("Acho que te intimidei demais... não entendi o que disse.\nVolte mais tarde!")