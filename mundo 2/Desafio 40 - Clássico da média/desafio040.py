n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media:.1f}')
    print(f'O aluno está APROVADO.')
elif media >= 5:
    print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media:.1f}')
    print(f'O aluno está em RECUPERAÇÃO.')
elif media < 5: 
    print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media:.1f}')
    print(f'O aluno está em REPROVADO.')
