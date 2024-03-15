cidade = str(input('em que cidade você nasceu? ')).strip()
cidade_1 = cidade.upper().split()
print('a cidade digitada se inicia com santo?', ('SANTO' in cidade_1 [0]))
