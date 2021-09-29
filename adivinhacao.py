import random

def jogar():

    print('********************')
    print('Jogo de adivinhação')
    print('********************')

    numero_secreto = random.randrange(1,101)
    rodada = 1
    numero_tentativas = 0
    pontos = 1000

    print('Selecione o nível: ', end='\n')

    nivel = int(input('1) Fácil 2) Médio 3) Difícil'))

    if(nivel == 1):
        numero_tentativas = 20
    elif (nivel == 2):
        numero_tentativas = 10
    else:
        numero_tentativas = 5

    #print(numero_secreto)
    #while(rodada <= numero_tentativas):

    for rodada in range(1,numero_tentativas + 1):


        print('Tentativa {} de {}' .format(rodada,numero_tentativas))

        chute = int(input('Digite um número entre 1 e 100: '))

        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100')
            continue

        if (chute == numero_secreto):
            print('Você acertou')
            break
        else:
            if(chute > numero_secreto):
                print('você errou, seu chute foi muito alto')
            elif (chute < numero_secreto):
                print('você errou, seu chute foi muito baixo')



           #rodada = rodada + 1
    pontos_perdidos = abs(chute - numero_secreto)   #pontos perdidos da rodada
    pontos = pontos - pontos_perdidos               #subtraindo os pontos perdidos da pontuação total
    print('Sua pontuação é {}'.format(pontos))
    print('Fim de jogo!')
