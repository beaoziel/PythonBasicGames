import random

tentativas = 0
numero_sorteado = random.randint(1,100)
numero_usuario = 0
continuar = True

def definirNivel():
    fim = False
    while fim == False:
        nivel = input("Qual nível você gostaria? (D or F)")
        if "D" in nivel.upper():
            tentativas = 5
            fim = True
        elif "F" in nivel.upper():
            tentativas = 10
            fim = True
        else:
            print("Desculpa... não entendi. ")
    return tentativas

def definirChances():
    return tentativas - 1

def verificar(sorteado, usuario):
    if usuario < sorteado:
        print(f"O número é maior que {usuario}")
        return False
    elif usuario > sorteado:
        print(f"O número é menor que {usuario}")
        return False
    else:
        return True

def jogar():
    numero_usuario = input("Qual número você gostaria de chutar?")
    try:
        numero_usuario = int(numero_usuario)
    except:
        print('Não é um número válido.')

    if isinstance(numero_usuario, int):
        return numero_usuario
    else:
        return -1

def definirJogada():
    global numero_usuario
    numero_usuario = jogar()
    if numero_usuario == -1:
        continuar = False
    else:
        continuar = True
    return continuar

#Main
tentativas = definirNivel()
while not tentativas == 0:
    while definirJogada() == False:
        definirJogada()
    else:
        if verificar(numero_sorteado, numero_usuario) == False:
            tentativas = definirChances()
            if tentativas == 0:
                print(f"Suas chances acabaram. O número era: {numero_sorteado}")
        else:
            print("Você ganhou!")
            continuar = False