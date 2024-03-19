import random
from time import sleep
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
escolha_computador = random.choice(opcoes)
print('Sua opção:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
escolha_jogador = int(input('Sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if escolha_computador == 'PEDRA' and escolha_jogador == 0:
    print('O computador escolheu: PEDRA')
    print('O jogador escolheu: PEDRA')
    print('EMPATE')
elif escolha_computador == 'PEDRA' and escolha_jogador == 1:
    print('O computador escolheu: PEDRA')
    print('O jogador escolheu: PAPEL')
    print('JOGADOR VENCEU')
elif escolha_computador == 'PEDRA' and escolha_jogador == 2:
    print('O computador escolheu PEDRA')
    print('O jogador escolheu TESOURA')
    print('COMPUTADOR VENCEU')
elif escolha_computador == 'PAPEL' and escolha_jogador == 0:
    print('O computador escolheu: PAPEL')
    print('O jogador escolheu: PEDRA')
    print('COMPUTADOR VENCEU')
elif escolha_computador == 'PAPEL' and escolha_jogador == 1:
    print('O computador escolheu: PAPEL')
    print('O jogador escolheu: PAPEL')
    print('EMPATE')
elif escolha_computador == 'PAPEL' and escolha_jogador == 2:
    print('O computador escolheu: PAPEL')
    print('O jogador escolheu: TESOURA')
    print('JOGADOR VENCEU')
elif escolha_computador == 'TESOURA' and escolha_jogador == 0:
    print('O computador escolheu: TESOURA')
    print('O jogador escolheu: PEDRA')
    print('JOGADOR VENCEU')
elif escolha_computador == 'TESOURA' and escolha_jogador == 1:
    print('O computador escolheu: TESOURA')
    print('O jogador escolheu: PAPEL')
    print('COMPUTADOR VENCEU')
elif escolha_computador == 'TESOURA' and escolha_jogador == 2:
    print('O computador escolheu: TESOURA')
    print('O jogador escolheu: TESOURA')
    print('EMPATE')
    