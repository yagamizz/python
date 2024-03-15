n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 > n3:
    print(f'MAIOR: {n1}')
    print(f'MENOR: {n3}')
if n1 > n3 > n2:
    print(f'MAIOR: {n1}')
    print(f'MENOR: {n2}')
if n2 > n1 > n3:
     print(f'MAIOR: {n2}')
     print(f'MENOR: {n3}')
if n2 > n3 > n1:
    print(f'MAIOR: {n2}')
    print(f'MENOR: {n1}')
if n3 > n1 > n2:
    print(f'MAIOR: {n3}')
    print(f'MENOR: {n2}')
if n3 > n2 > n1:
    print(f'MAIOR: {n3}')
    print(f'MENOR: {n1}')
