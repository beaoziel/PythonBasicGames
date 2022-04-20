import random
frutas = [
    {"Nome": "Banana",
     "Posicao": 1},
    {"Nome": "Maçã",
     "Posicao": 2},
    {"Nome": "Laranja",
     "Posicao": 3},
    {"Nome": "Mamão",
     "Posicao": 4},
    {"Nome": "Manga",
     "Posicao": 5},
    {"Nome": "Açaí",
     "Posicao": 6},
    {"Nome": "Melancia",
     "Posicao": 7},
    {"Nome": "Tangerina",
     "Posicao": 8},
    {"Nome": "Abacaxi",
     "Posicao": 9},
    {"Nome": "Uva",
     "Posicao": 10},
]
pontos = 0
parar = False
escolha = 0
opcao1 = 0
opcao2 = 0

def sortear():
    return random.randint(0, len(frutas)) - 1

def checarValores(opcao1, opcao2):
    if opcao1 == opcao2:
        while opcao1 == opcao2:
            opcao1 = sortear()
            opcao2 = sortear()

    p1 = frutas[opcao1]
    p2 = frutas[opcao2]
    print(f"Opcão 1: {p1['Nome']}\nOpção 2: {p2['Nome']}")

def comparar(opcao1, opcao2):
    vencedor = 0
    p1 = frutas[opcao1]
    p2 = frutas[opcao2]

    if p1['Posicao'] > p2['Posicao']:
        vencedor = 2
    else:
        vencedor = 1

    return vencedor

def jogar():
    escolha = input("- Qual o vencedor? ")
    try:
        escolha = int(escolha)
    except:
        print('Não é um número válido.')

    if isinstance(escolha, int):
        if escolha < 1 or escolha > 2:
            print('Não é uma opção válida.')
            return -1
        else:
            return escolha
    else:
        return -1


#Main
opcao1 = sortear()
opcao2 = sortear()

while parar == False:
    checarValores(opcao1, opcao2)

    escolha = jogar()
    while escolha == -1:
        escolha = jogar()

    if comparar(opcao1, opcao2) == escolha:
        pontos += 1
        print("Certa resposta! ")
        if escolha == 1:
            opcao2 = sortear()
        else:
            opcao1 = sortear()

    else:
        print(f"Resposta errada. \nFim de jogo. Você conseguiu {pontos} pontos.")
        parar = True