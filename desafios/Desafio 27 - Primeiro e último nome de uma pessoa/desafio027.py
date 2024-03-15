nome = str(input('Digite seu nome completo: ')).strip()
nome_dividido = nome.split()
primeiro_nome = nome_dividido [0]
ultimo_nome = nome_dividido [-1]
print(f'Primeiro nome: {primeiro_nome}')
print(f'Último nome: {ultimo_nome}')
