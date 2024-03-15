import random
num = random.randint(0, 5)
chute = int(input('Digite um número de 0 a 5: '))
if chute == num:
    print(f'Parabéns, você acertou! "{num}"')
else:
    print(f'Você errou! O número era {num}')
