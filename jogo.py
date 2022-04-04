import random
import calculos

cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deck1 = []
deck2 = []

def sortear(deck):
    carta = random.choice(cartas)
    deck.append(carta)
    print("Carta sorteada: ", carta)

def comecar():
    count = 0
    while count <= 3:
        if count == 0 or count == 2:
            deck1.append(random.choice(cartas))
        else:
            deck2.append(random.choice(cartas))
        count = count + 1

def somar(deck):
    soma = 0
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    #Fomrma somando item por item, com objetivo de práticar debugging
    for i in range(len(deck)) :
        soma += deck[i]
    return soma

def blackjack(continuar):
    jogadorVitoria = False
    computadorVitoria = False

    if somar(deck1) == 21 and 1 or 11 in deck1: #Se a soma cair
        jogadorVitoria = True
    elif somar(deck2) == 21 and 1 or 11 in deck2:
        computadorVitoria = True

    if jogadorVitoria == True and computadorVitoria == True:
        print("Empate! Fim de jogo.")
        continuar = False
    elif computadorVitoria == True:
        print(f"BLACKJACK!\n Poxa! O computador ganhou o jogo.")
        continuar = False
        calculos.blackjack(vitoria=False)
    elif jogadorVitoria == True:
        print(f"BLACKJACK!\n Parabéns! Você ganhou o jogo. Cartas do computador: {deck2}\nSuas cartas: {deck1} ")
        continuar = False
        calculos.blackjack(vitoria=True)
    else:
        continuar = True
    return continuar

def checarValores(continuar):
    if somar(deck1) >= 21:
        continuar = False
    elif somar(deck2) >= 21:
        continuar = False
    return continuar

def fim():
    vitoria = False
    print(f"Suas cartas: {deck1}, você conseguiu {somar(deck1)} pontos!\n"
          f"Cartas do computador: {deck2}, conseguindo {somar(deck2)} pontos.")

    if somar(deck1) > somar(deck2):
        print("Parabéns! Você ganhou :)")
        vitoria = True
        calculos.calculo(vitoria)
    elif somar(deck2) > somar(deck1):
        print("Poxa! O computador venceu dessa vez...")
        vitoria = False
        calculos.calculo(vitoria)
    else:
        print("Empate!")
