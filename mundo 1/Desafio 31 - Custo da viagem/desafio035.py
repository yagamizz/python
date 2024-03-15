d = int(input('Qual a distância da viagem em KM? '))
valor_viagens_curtas = d * 0.50
valor_viagens_longas = d * 0.45
if d > 200:
    print(f'sua viagem de {d} KM terá um valor de R${valor_viagens_longas:.2f}')
else:
    print(f'sua viagem de {d} KM terá um valor de R${valor_viagens_curtas:.2f}')
