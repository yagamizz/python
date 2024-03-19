import random

def jogo():
    opcoes = ["Pedra", "Papel", "Tesoura"]

    # Mapeamento de opções numéricas para Pedra, Papel e Tesoura
    opcoes_numeros = {"0": "Pedra", "1": "Papel", "2": "Tesoura"}

    jogada_computador = random.choice(opcoes)

    print("Escolha sua jogada:")
    print("0: Pedra")
    print("1: Papel")
    print("2: Tesoura")

    # Solicitação da escolha do usuário usando opções numéricas
    escolha_usuario = input("Digite o número correspondente à sua jogada: ")

    # Verifica se a escolha do usuário é válida
    if escolha_usuario not in opcoes_numeros:
        print("Escolha inválida. Tente novamente.")
        jogo()

    jogada_usuario = opcoes_numeros[escolha_usuario]

    print("Você escolheu:", jogada_usuario)
    print("O computador escolheu:", jogada_computador)

    if jogada_usuario == jogada_computador:
        print("Empate!")
    elif (jogada_usuario == "Pedra" and jogada_computador == "Tesoura") or \
         (jogada_usuario == "Tesoura" and jogada_computador == "Papel") or \
         (jogada_usuario == "Papel" and jogada_computador == "Pedra"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    jogar_novamente = input("Quer jogar novamente? (Sim/Não): ").capitalize()
    if jogar_novamente == "Sim":
        jogo()
    else:
        print("Obrigado por jogar!")

# Iniciar o jogo
jogo()
