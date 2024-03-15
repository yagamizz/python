from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você deve se alistar imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + idade
    print(f'Você não tem 18 anos. Ainda faltam {saldo} para você estar apto ao alistamento.')
    print(f'Seu alistamento será em {ano}.')
else:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você já deveria ter se alistasdo há {saldo} anos.')
    print(f'Seu alistamento foi em {ano}')
