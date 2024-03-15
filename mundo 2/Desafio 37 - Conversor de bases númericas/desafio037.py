num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print(f'{num} convertido para BINÁRIO é igual a \033[30m{bin(num)[2:]}\033[m')
elif escolha == 2:
    print(f'{num} convertido para OCTAL é igual a \033[31m{oct(num)[2:]}\033[m')
elif escolha == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a \033[32m{hex(num)[2:]}\033[m')
else:
    print('Opção inválida, tente novamente.')
