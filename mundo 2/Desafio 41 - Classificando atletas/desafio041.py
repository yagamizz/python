from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade < 6:
    print('Idade não elegível para classificação.')
    print(f'"{idade}"')
elif idade >= 6 and idade <= 9:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: MIRIM.')
elif idade >= 10 and idade <= 14:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: INFANTIL.')
elif idade >= 15 and idade <= 19:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: JUNIOR.')
elif idade >= 20 and idade <= 25:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: SÊNIOR.')
else: 
    print(f'O atleta tem {idade} anos.')
    print('Classificação: MASTER.')
