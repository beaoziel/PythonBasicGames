aposta1 = 0.0
aposta2 = 0.0

def calculo(vitoria):
    saldo = 0
    if vitoria == True:
        saldo = float(aposta1) * 2
    elif vitoria == False:
        saldo = float(aposta1) - float(aposta2) * 2

    print("Valor inicial: R$" + str(aposta1) + "\n"
           "Valor final: R$" + str(saldo))

def blackjack(vitoria):
    saldo = 0
    if vitoria == True:
        saldo = float(aposta1) * 1.5
    else:
        saldo = float(aposta2) * 1.5 - float(aposta1)

    print("Valor inicial: R$" + str(aposta1) + "\n"
    "Valor final: R$" + str(saldo))