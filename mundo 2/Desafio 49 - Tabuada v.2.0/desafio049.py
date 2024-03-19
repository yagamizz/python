n = int(input('Digite o número que você quer ver a tabuada: '))
e = int(input('Digite até que número você quer que seja multiplicado: '))
for c in range(1, e + 1):
    print(f'{n} x {c} = {n * c}')